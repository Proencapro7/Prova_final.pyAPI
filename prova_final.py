import requests 
import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title('APP API')
        self.root.geometry('1000x800')

        self.label = tk.Label(self.root, text='Busca API')
        self.label.pack(pady=10)

        self.fetch_button = tk.Button(self.root, text='Aperte Aqui', command=self.fetch_data)
        self.fetch_button.pack(pady=10)

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(pady=50)

    def fetch_data(self):
        try:
            response = requests.get("https://df2ff082-6ef8-470b-ba48-ebcdf9978c31-00-2fx7uri5s6mnp.riker.replit.dev/compositor")
            if response.status_code == 200:
                data = response.json()
                self.listbox.delete(0, tk.END)
                for user in data: 
                    self.listbox.insert(tk.END, user)
            else:
                messagebox.showerror('Falha', f'Erro {response.status_code}: Não foi possível acessar a API.')
        
        except requests.exceptions.RequestException as e:
            messagebox.showerror('Falha ao conectar', f'Erro de conexão: {str(e)}')


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
