def evaluate_employee_performance():
    # Define variables
    employee_id = int(input("Enter Employee ID: "))
    productivity = int(input("Enter Productivity Rating (1-10): "))
    efficiency = int(input("Enter Efficiency Rating (1-10): "))
    reliability = int(input("Enter Reliability Rating (1-10): "))
    	
    # Calculate performance score
    performance_score = (productivity + efficiency + reliability) / 3
    
    # Display the results
    print("\n--- Employee Performance Evaluation ---")
    print(f"Employee ID: {employee_id}")
    print(f"Productivity: {productivity}")
    print(f"Efficiency: {efficiency}")
    print(f"Reliability: {reliability}")
    print(f"Performance Score: {performance_score:.2f}")
evaluate_employee_performance()