class operation:
    def __init__(self,data , time_op):
        self.op_name=data
        self.op_time=time_op
        self.next = None


class queue:
    def __init__(self):
        self.first=None
        self.last = None

    def push(self,data,time_op):
        item=operation(data,time_op)
        if self.first is None:
            self.first = self.last=item
        else:
            self.last.next = item
            self.last = item

    def pop(self):
        if self.first is None:
            # print("There is any operation to delete")
            return
        curr = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return curr

    def is_empty(self):
        return self.first is None

    def display(self):
        if self.first is None:
            print("No nodes found")
        else:
            curr=self.first
            while curr:
                print("The operation is: "+curr.op_name +" and the time is: " + str(curr.op_time))
                curr=curr.next


    def round_robn(self,qauntum):
        if self.first is None:
            print("You must fill the queue first.")
            return

        print("=======================================")
        print("\nScheduling operations by Round Robin:")
        print("=======================================")
        print("Operation\tImplementation Time\t  Waiting Time\tEnd Time")
        print("___________________________________________________")
        total = 0
        waiting_time = {}
        end_time={}
        while not self.is_empty():
            curr=self.pop()
            if  curr.op_time  > qauntum:
                total+=qauntum
                remaining_time=curr.op_time-qauntum
                self.push(curr.op_name , remaining_time)
            else:
                total+=curr.op_time
                end_time[curr.op_name]=total
                waiting_time[curr.op_name]=total-curr.op_time
                print(f"{curr.op_name}\t\t\t{curr.op_time}\t\t\t\t\t  {waiting_time}\t\t\t{end_time}")
                print("___________________________________________________")
        avg_waiting=sum(waiting_time.values())/len(waiting_time)
        avg_end=sum(end_time.values())/len(end_time)
        print(f"\nAverage waiting time: {avg_waiting:.2f}")
        print(f"Average expiry time: {avg_end:.2f}")


def main():
    q=queue()
    operation=int(input("Enter the number of operation: "))
    for i in range(operation):
        data = input(f"Enter the operation name {i+1}: ")
        time=int(input(f"Enter the time for operation {i+1}: "))
        q.push(data,time)
    # q.display()
    qauntum = int(input("Enter the qauntum time: "))
    q.round_robn(qauntum)

main()



