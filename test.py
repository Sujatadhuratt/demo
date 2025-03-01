import psutil

# Function to get top 5 CPU-consuming processes
def get_top_cpu_processes():
    # Create a list of all processes sorted by CPU usage
    processes = [(proc.info['pid'], proc.info['name'], proc.info['cpu_percent'])
                 for proc in psutil.process_iter(['pid', 'name', 'cpu_percent'])]

    # Sort the processes by CPU usage in descending order
    processes.sort(key=lambda x: x[2], reverse=True)

    # Display the top 5 processes
    print(f"{'PID':<10} {'Process Name':<30} {'CPU Usage (%)'}")
    print("="*50)
    
    for proc in processes[:5]:
        print(f"{proc[0]:<10} {proc[1]:<30} {proc[2]:<15}")

if __name__ == "__main__":
    get_top_cpu_processes()
