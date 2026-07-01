python
import random
import tkinter as tk

class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("数当てゲーム")
        self.root.geometry("1065x600")

        self.selectNunber = random.randint(1, 100)

        self.initUi()

    def initUi(self):
        self.labelInfo = tk.Label(self.root, text="1～100の数字を入れてね")
        self.inputBox = tk.Entry(self.root)

        self.button = tk.Button(self.root, text="回答", command=self.juageNumber)
        self.resurut = tk.Label(self.root, text="", fg="#0b37af")

        self.labelInfo.pack(pady=5)
        self.inputBox.pack(pady=5)
        self.button.pack(pady=5)
        self.resurut.pack(pady=5)

    def juageNumber(self):
        self.userInput = self.inputBox.get()
        if not self.userInput.isdigit():
            self.resurut.config(text="数字を入力してね")
            return
        
        guess = int(self.userInput)
        
        if guess < self.selectNunber:
            self.resurut.config(text="正解よりも小さいよ", fg="#0b37af")

        elif guess > self.selectNunber:
            self.resurut.config(text="正解よりも大きいよ", fg="#0b37af")

        else:
            self.resurut.config(text="正解!", fg="#0baf5d")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessGame(root)
    root.mainloop()
