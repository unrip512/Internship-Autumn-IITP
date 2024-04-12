from fastapi import FastAPI
from core.system import System

def get_application():
    app = FastAPI()
    my_system = System()

    @app.post("/api/start")
    def start_system():  # система автоматически запустится
        my_system.start()
        return 'System has been started'

    @app.get("/api/system_condition")
    def system_condition(
            gate_id: int):  # принимает значение gate_id от 1 до 64, если передано 0, то вернет массив кол-ва срабатываний всех клапанов
        return my_system.logger.get_state(gate_id)

    @app.put("/api/stop")
    def stop_process():
        a = my_system.stop()
        return f"process was stopped"

    return app



