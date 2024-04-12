import multiprocessing
import time
from fastapi import FastAPI
import random
from typing import List

GATES_COUNT = 64
app = FastAPI()

class GatesLogger:
    # static variables - почитай что это такое если не знаешь
    # tmp -multiprocessing.Array с количеством срабатываний
    # каждого из 64 клапанов, если что клапан я называю - gates
    # Прочитай как в библиотеке multiprocessing создавать процессы,
    # а также что это за массив такой интересный
    tmp = multiprocessing.Array('i', GATES_COUNT)

    # multiprocessing - модуль многопроцессорной обработки. Позволяет разделить независимо выполняемые вычисления между доступными ядрами процессора.
    # mlp.Array(typecode_or_type,size_of_init) - массив, выделенный из общей памяти, к которому есть доступ у  (...который явл общим для...) всех процессов.
    # Если второй агрумент - целое число n,то создаться массив из n эллементов, заполненный нулями

    def __init__(self):
        pass

    def log_trigger(self, gate_id):      #Сообщить логгеру что клапан сработал; param gate_id: идентификатор клапана

        self.tmp[gate_id] = self.tmp[gate_id] + 1

        return 0

    def get_state(self, gate_id):
        # принимает gate_id от 1 до 64. Если предать 0, то вернет массив значений срабатываний всех клапанов

        if gate_id == 0:
            return self.tmp[:]
        else:
            return self.tmp[gate_id - 1]


class System:
    def __init__(self):
        """
        gate_process - multiprocessing.Process процесс в котором будут работать клапаны
        in_work - переменная к которой сможет обращаться процесс чтобы понять, нужно ли ему работать или нет
        logger - логгер которому ты будешь сообщать информацию об открытии клапанов
        """

        self.gate_process = None
        self.is_work = multiprocessing.Value('b', 0)

        self.logger = GatesLogger()
        print("I am an object of class System and I was created")

    def _gate_thread(self):
        """
        Процесс который запускает клапаны
        Алгоритм:
        1) Процесс уходит в sleep на время от 1 до 10 секунд которое ты генеришь случайно
        2) Затем происходит генерация рандомного числа gates_count от 0 до 64 -
           это количество клапанов, которое сработает
        3) Затем происходит генерация gates_count рандомных целых различных
           чисел от 0 до 63 это номера клапанов которые сработают
        """

        while True:
            sleep_time = random.randint(1, 10)
            print('sleep_time = ', sleep_time)
            time.sleep(sleep_time)

            gates_count = random.randint(0, 64)
            #print('gate_count =', gates_count)

            gates_id = list(range(64))
            triggered_gates_id = random.sample(gates_id, gates_count)

            #print("the following gates are going to work:", [i + 1 for i in triggered_gates_id])

            for i in triggered_gates_id:
                self.logger.log_trigger(i)

            #!!!!!!!!!!!!!!!!!!!!! УБРАТЬ ПОТОМ!!!!!!!!!!!!
            print(self.logger.get_state(0)) # после каждого круга срабатываний будет печатать состояние системы


    def start(self):

        self.is_work.value = 1

        if self.is_work.value == 1:
            self.gate_process = multiprocessing.Process(target=self._gate_thread)
            print('A process was created')
            self.gate_process.start()
            return 0
        else:
            return 1


    def stop(self): # !!!!!!!!!!!ПРОПИСАТЬ ЧТО ДЕЛАЕТ ФУНКЦИЯ END И КАКИЕ КОДЫ ВОЗВРАЩАЕТ
        """
        Выключение системы:
        1) Остановка процесса управления клапанами _gate_thread

        :return:
        """
        if not self.gate_process:        #проверка, на None
            return 1
        else:
            if self.gate_process.is_alive():
                self.gate_process.terminate()
                return 0
            else:
                return 1

#db: List[System] = []
db = multiprocessing.Array(System, 1)

@app.post("/api/create")
async def create_system(): #система автоматически запустится

    len_of_db = len(db)
    if len_of_db > 0:
        print('the system has already been created')
        return -1
    else:
        sys = System()
        db.append(sys)
        len_of_db = len(db)
        print('System has been created with id', len_of_db - 1)
        sys.start()
        return (f"number of created system: {len_of_db - 1}")    #возвращает номер созданной системы


@app.get("/api/condition")
async def system_condition(system_id, gate_id):
    #принимает значение gate_id от 1 до 64, если передано 0, то вернет массив кол-ва срабатываний всех клапанов
    mas = db[system_id].logger.get_state(gate_id)
    return mas


@app.delete("/api/delete")
async def stop_process(system_id):
    a = db[system_id].stop()
    return a


@app.get("/")
async def root():
    return {'Hello': 'world'}

#system_id = create_system()
#print('system_id =', system_id)
#print('condition of gates:', system_condition(system_id, 0))
#time.sleep(60)
#stop_process(system_id)
#print('condition of gates:', system_condition(system_id, 0))

