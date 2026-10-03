from datetime import datetime, timedelta

class Treino:
    def __init__(self, id_treino, data, distancia, tempo):
        self._id = id_treino
        self._data = data          # datetime
        self._distancia = distancia  # float (km)
        self._tempo = tempo        # timedelta

    # Getters e Setters
    def get_id(self): return self._id
    def set_id(self, id_treino): self._id = id_treino

    def get_data(self): return self._data
    def set_data(self, data): self._data = data

    def get_distancia(self): return self._distancia
    def set_distancia(self, distancia): self._distancia = distancia

    def get_tempo(self): return self._tempo
    def set_tempo(self, tempo): self._tempo = tempo

    def pace(self):
        if self._distancia <= 0:
            return "00:00"
        total_segundos = self._tempo.total_seconds()
        segundos_por_km = total_segundos / self._distancia
        minutos = int(segundos_por_km // 60)
        segundos = int(segundos_por_km % 60)
        return f"{minutos:02d}:{segundos:02d} min/km"

    def __str__(self):
        data_str = self._data.strftime("%d/%m/%Y")
        return f"ID: {self._id} | Data: {data_str} | Distância: {self._distancia:.2f}km | Tempo: {self._tempo} | Pace: {self.pace()}"


class TreinoUI:
    def __init__(self):
        self.treinos = []

    def main(self):
        while True:
            print("\n--- MENU TREINO ---")
            print("1 - Inserir treino")
            print("2 - Listar todos os treinos")
            print("3 - Listar treino por ID")
            print("4 - Atualizar treino")
            print("5 - Excluir treino")
            print("6 - Treino mais rápido")
            print("0 - Sair")
            opcao = input("Opção: ")

            if opcao == "1": self.inserir()
            elif opcao == "2": self.listar()
            elif opcao == "3": self.listar_id()
            elif opcao == "4": self.atualizar()
            elif opcao == "5": self.excluir()
            elif opcao == "6": self.mais_rapido()
            elif opcao == "0": break
            else: print("Opção inválida!")

    def inserir(self):
        id_treino = int(input("ID: "))
        data_txt = input("Data (dd/mm/aaaa): ")
        data = datetime.strptime(data_txt, "%d/%m/%Y")
        distancia = float(input("Distância (km): "))
        h, m, s = map(int, input("Tempo (HH:MM:SS): ").split(":"))
        tempo = timedelta(hours=h, minutes=m, seconds=s)

        t = Treino(id_treino, data, distancia, tempo)
        self.treinos.append(t)
        print("Treino inserido!")

    def listar(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.")
        for t in self.treinos:
            print(t)

    def listar_id(self):
        id_busca = int(input("ID do treino: "))
        for t in self.treinos:
            if t.get_id() == id_busca:
                print(t)
                return
        print("Treino não encontrado.")

    def atualizar(self):
        id_busca = int(input("ID do treino a atualizar: "))
        for t in self.treinos:
            if t.get_id() == id_busca:
                data_txt = input("Nova Data (dd/mm/aaaa): ")
                t.set_data(datetime.strptime(data_txt, "%d/%m/%Y"))
                t.set_distancia(float(input("Nova Distância (km): ")))
                h, m, s = map(int, input("Novo Tempo (HH:MM:SS): ").split(":"))
                t.set_tempo(timedelta(hours=h, minutes=m, seconds=s))
                print("Treino atualizado!")
                return
        print("Treino não encontrado.")

    def excluir(self):
        id_busca = int(input("ID do treino a excluir: "))
        for t in self.treinos:
            if t.get_id() == id_busca:
                self.treinos.remove(t)
                print("Treino excluído!")
                return
        print("Treino não encontrado.")

    def mais_rapido(self):
        if not self.treinos:
            print("Nenhum treino cadastrado.")
            return
        
        mais_rapido = self.treinos[0]
        menor_pace_segundos = mais_rapido.get_tempo().total_seconds() / mais_rapido.get_distancia()

        for t in self.treinos:
            pace_atual = t.get_tempo().total_seconds() / t.get_distancia()
            if pace_atual < menor_pace_segundos:
                menor_pace_segundos = pace_atual
                mais_rapido = t

        print("--- TREINO MAIS RÁPIDO ---")
        print(mais_rapido)


if __name__ == "__main__":
    app = TreinoUI()
    app.main()