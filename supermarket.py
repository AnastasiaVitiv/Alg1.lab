class SupermarketQueue:
    def __init__(self):
        self.queue = []

    def arrive(self, customer_name):
        self.queue.append(customer_name)

    def serve(self):
        while self.queue:
            customer = self.queue.pop(0)
            print(f"Обслуговується: {customer}")


    def display_queue(self):
        if not self.queue:
            print("Каса вільна")
        else:
            print("Поточна черга:", " -> ".join(self.queue))

supermarket = SupermarketQueue()
supermarket.arrive("Віка")
supermarket.arrive("Настя")
supermarket.arrive("Таня")

supermarket.display_queue()
supermarket.serve()
supermarket.display_queue()
