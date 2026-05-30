from car_functions import CarDashboardUI

def main() -> None:
    # Instantiate UI controller system to initialize verification checks and dashboard loops
    dashboard = CarDashboardUI()
    dashboard.launch_dashboard()

if __name__ == "__main__":
    main()