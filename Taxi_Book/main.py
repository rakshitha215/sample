from typing import List

POINTS = ['A', 'B', 'C', 'D', 'E', 'F']
DISTANCE_BETWEEN_POINTS = 15   # km
TIME_BETWEEN_POINTS = 1        # hour

class Booking:
    booking_counter = 1

    def __init__(self, customer_id, pickup, drop, pickup_time, drop_time, amount):
        self.booking_id = Booking.booking_counter
        Booking.booking_counter += 1

        self.customer_id = customer_id
        self.pickup = pickup
        self.drop = drop
        self.pickup_time = pickup_time
        self.drop_time = drop_time
        self.amount = amount


class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id
        self.current_location = 'A'
        self.free_time = 0
        self.total_earnings = 0
        self.bookings: List[Booking] = []

    def is_free(self, pickup_time):
        return self.free_time <= pickup_time

    def calculate_distance(self, from_point, to_point):
        return abs(POINTS.index(from_point) - POINTS.index(to_point)) * DISTANCE_BETWEEN_POINTS

    def calculate_fare(self, distance):
        if distance <= 5:
            return 100
        return 100 + (distance - 5) * 10

    def book_taxi(self, customer_id, pickup, drop, pickup_time):
        distance = self.calculate_distance(pickup, drop)
        travel_time = abs(POINTS.index(pickup) - POINTS.index(drop)) * TIME_BETWEEN_POINTS
        drop_time = pickup_time + travel_time

        amount = self.calculate_fare(distance)

        booking = Booking(customer_id, pickup, drop, pickup_time, drop_time, amount)

        self.bookings.append(booking)
        self.total_earnings += amount
        self.current_location = drop
        self.free_time = drop_time

        return booking


class TaxiBookingSystem:
    def __init__(self, n):
        self.taxis = [Taxi(i+1) for i in range(n)]

    def find_taxi(self, pickup_point, pickup_time):
        free_taxis = []

        for taxi in self.taxis:
            if taxi.is_free(pickup_time):
                distance_to_pickup = abs(POINTS.index(taxi.current_location) - POINTS.index(pickup_point))
                free_taxis.append((distance_to_pickup, taxi.total_earnings, taxi))

        if not free_taxis:
            return None

        # Sort by nearest distance and then by lowest earnings
        free_taxis.sort(key=lambda x: (x[0], x[1]))

        return free_taxis[0][2]

    def book_taxi(self, customer_id, pickup, drop, pickup_time):
        taxi = self.find_taxi(pickup, pickup_time)

        if not taxi:
            print("Booking Rejected. No Taxi Available.")
            return

        booking = taxi.book_taxi(customer_id, pickup, drop, pickup_time)

        print("Taxi can be allotted.")
        print(f"Taxi-{taxi.taxi_id} is allotted")

    def display_details(self):
        for taxi in self.taxis:
            if taxi.bookings:
                print(f"\nTaxi-{taxi.taxi_id}    Total Earnings: Rs. {taxi.total_earnings}")
                print("BookingID  CustomerID  From  To  Pickup  Drop  Amount")

                for booking in taxi.bookings:
                    print(f"{booking.booking_id}\t   {booking.customer_id}\t\t"
                          f"{booking.pickup}\t {booking.drop}\t "
                          f"{booking.pickup_time}\t {booking.drop_time}\t {booking.amount}")

if __name__ == "__main__":
    system = TaxiBookingSystem(4)

    system.book_taxi(1, 'A', 'B', 9)
    system.book_taxi(2, 'B', 'D', 9)
    system.book_taxi(3, 'B', 'C', 12)

    system.display_details()
