import multiprocessing
import time
from fastapi import FastAPI
import random

GATES_COUNT = 64
app = FastAPI()

class GatesLogger:

    tmp = multiprocessing.Array('i', GATES_COUNT)

    # multiprocessing - модуль многопроцессорной обработки. Позволяет разделить независимо выполняемые вычисления между доступными ядрами процессора.
    # mlp.Array(typecode_or_type,size_of_init) - массив, выделенный из общей памяти, к которому есть доступ у  (...который явл общим для...) всех процессов.
    # Если второй агрумент - целое число n,то создаться массив из n эллементов, заполненный нулями

    def __init__(self):
        pass

    def log_trigger(self, gate_id):    #Сообщить логгеру что клапан сработал; param gate_id: идентификатор клапана

        self.tmp[gate_id] = self.tmp[gate_id] + 1

        return 0

    def get_state(self, gate_id):

        if gate_id == 0:
            return self.tmp[:]
        else:
            return self.tmp[gate_id - 1]


class System:
    def __init__(self):

        self.gate_process = None
        self.is_work = multiprocessing.Value('b', 0)

        self.logger = GatesLogger()
        print("I am an object of class System and I was created")

    def _gate_thread(self):
        """

        """

        for i in range(10):
            sleep_time = random.randint(1, 10)
            print('sleep_time = ', sleep_time)
            time.sleep(sleep_time)

            gates_count = random.randint(0, 64)

            gates_id = list(range(64))
            triggered_gates_id = random.sample(gates_id, gates_count)

            for i in triggered_gates_id:
                self.logger.log_trigger(i)

    def start(self):

        self.is_work.value = 1

        if self.is_work.value == 1:
            self.gate_process = multiprocessing.Process(target=self._gate_thread)
            self.gate_process.start()
            return 0
        else:
            return 1

    def stop(self):

        if not self.gate_process:
            return 1
        else:
            if self.gate_process.is_alive():
                self.gate_process.terminate()
                return 0
            else:
                return 2


my_system = System()


@app.post("/api/start")
async def start_system(): #система автоматически запустится
        my_system.start()
        return 'System has been created'


@app.get("/api/system_condition")
async def system_condition(gate_id: int):       #принимает значение gate_id от 1 до 64, если передано 0, то вернет массив кол-ва срабатываний всех клапанов
    return my_system.logger.get_state(gate_id)


@app.put("/api/stop")
async def stop_process():
    a = my_system.stop()
    return f"process was stopped with code {a}"

