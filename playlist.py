from datetime import datetime, timedelta

class Musica:
    def __init__(self, id_musica, titulo, artista, album, duracao):
        self._id = id_musica
        self._titulo = titulo
        self._artista = artista
        self._album = album
        self._duracao = duracao  # timedelta

    def get_id(self): return self._id
    def set_id(self, v): self._id = v
    def get_titulo(self): return self._titulo
    def set_titulo(self, v): self._titulo = v
    def get_artista(self): return self._artista
    def set_artista(self, v): self._artista = v
    def get_album(self): return self._album
    def set_album(self, v): self._album = v
    def get_duracao(self): return self._duracao
    def set_duracao(self, v): self._duracao = v

    def __str__(self):
        return f"ID: {self._id} | Título: {self._titulo} | Artista: {self._artista} | Duração: {self._duracao}"


class PlayList:
    def __init__(self, id_playlist, nome, descricao):
        self._id = id_playlist
        self._nome = nome
        self._descricao = descricao

    def get_id(self): return self._id
    def set_id(self, v): self._id = v
    def get_nome(self): return self._nome
    def set_nome(self, v): self._nome = v
    def get_descricao(self): return self._descricao
    def set_descricao(self, v): self._descricao = v

    def tempo_total(self, lista_itens, lista_musicas):
        total = timedelta()
        for item in lista_itens:
            if item.get_id_playlist() == self._id:
                for m in lista_musicas:
                    if m.get_id() == item.get_id_musica():
                        total += m.get_duracao()
        return total

    def __str__(self):
        return f"ID: {self._id} | Nome: {self._nome} | Descrição: {self._descricao}"


class PlayListItem:
    def __init__(self, id_item, id_playlist, id_musica, data_inclusao, sequencia):
        self._id = id_item
        self._id_playlist = id_playlist
        self._id_musica = id_musica
        self._data_inclusao = data_inclusao  # datetime
        self._sequencia = sequencia          # int

    def get_id(self): return self._id
    def set_id(self, v): self._id = v
    def get_id_playlist(self): return self._id_playlist
    def set_id_playlist(self, v): self._id_playlist = v
    def get_id_musica(self): return self._id_musica
    def set_id_musica(self, v): self._id_musica = v
    def get_data_inclusao(self): return self._data_inclusao
    def set_data_inclusao(self, v): self._data_inclusao = v
    def get_sequencia(self): return self._sequencia
    def set_sequencia(self, v): self._sequencia = v

    def __str__(self):
        dt = self._data_inclusao.strftime("%d/%m/%Y %H:%M")
        return f"Item ID: {self._id} | Playlist ID: {self._id_playlist} | Música ID: {self._id_musica} | Seq: {self._sequencia} | Data: {dt}"


class UI:
    def __init__(self):
        self.playlists = []
        self.musicas = []
        self.itens = []

    def main(self):
        while True:
            print("\n--- MENU PLAYLIST ---")
            print("1 - Cadastrar Playlist | 2 - Listar Playlists | 3 - Atualizar Playlist | 4 - Excluir Playlist")
            print("5 - Cadastrar Música   | 6 - Listar Músicas   | 7 - Atualizar Música   | 8 - Excluir Música")
            print("9 - Add Música na Playlist | 10 - Listar Itens | 11 - Remover Item | 0 - Sair")
            op = input("Opção: ")

            if op == "1": self.inserir_playlist()
            elif op == "2": self.listar_playlists()
            elif op == "3": self.atualizar_playlist()
            elif op == "4": self.excluir_playlist()
            elif op == "5": self.inserir_musica()
            elif op == "6": self.listar_musicas()
            elif op == "7": self.atualizar_musica()
            elif op == "8": self.excluir_musica()
            elif op == "9": self.inserir_item()
            elif op == "10": self.listar_itens()
            elif op == "11": self.excluir_item()
            elif op == "0": break

    # Métodos de Playlist
    def inserir_playlist(self):
        id_p = int(input("ID Playlist: "))
        nome = input("Nome: ")
        desc = input("Descrição: ")
        self.playlists.append(PlayList(id_p, nome, desc))

    def listar_playlists(self):
        for p in self.playlists:
            tempo = p.tempo_total(self.itens, self.musicas)
            print(f"{p} | Tempo Total: {tempo}")

    def atualizar_playlist(self):
        id_p = int(input("ID Playlist: "))
        for p in self.playlists:
            if p.get_id() == id_p:
                p.set_nome(input("Novo Nome: "))
                p.set_descricao(input("Nova Descrição: "))
                return

    def excluir_playlist(self):
        id_p = int(input("ID Playlist: "))
        self.playlists = [p for p in self.playlists if p.get_id() != id_p]
        self.itens = [i for i in self.itens if i.get_id_playlist() != id_p]

    # Métodos de Música
    def inserir_musica(self):
        id_m = int(input("ID Música: "))
        t = input("Título: ")
        a = input("Artista: ")
        alb = input("Álbum: ")
        m, s = map(int, input("Duração (MM:SS): ").split(":"))
        dur = timedelta(minutes=m, seconds=s)
        self.musicas.append(Musica(id_m, t, a, alb, dur))

    def listar_musicas(self):
        for m in self.musicas:
            print(m)

    def atualizar_musica(self):
        id_m = int(input("ID Música: "))
        for m in self.musicas:
            if m.get_id() == id_m:
                m.set_titulo(input("Novo Título: "))
                m.set_artista(input("Novo Artista: "))
                m.set_album(input("Novo Álbum: "))
                minu, seg = map(int, input("Nova Duração (MM:SS): ").split(":"))
                m.set_duracao(timedelta(minutes=minu, seconds=seg))
                return

    def excluir_musica(self):
        id_m = int(input("ID Música: "))
        self.musicas = [m for m in self.musicas if m.get_id() != id_m]
        self.itens = [i for i in self.itens if i.get_id_musica() != id_m]

    # Métodos de Itens
    def inserir_item(self):
        id_i = int(input("ID Item: "))
        id_p = int(input("ID Playlist: "))
        id_m = int(input("ID Música: "))
        seq = int(input("Sequência: "))
        item = PlayListItem(id_i, id_p, id_m, datetime.now(), seq)
        self.itens.append(item)

    def listar_itens(self):
        for i in self.itens:
            print(i)

    def excluir_item(self):
        id_i = int(input("ID Item: "))
        self.itens = [i for i in self.itens if i.get_id() != id_i]


if __name__ == "__main__":
    app = UI()
    app.main()