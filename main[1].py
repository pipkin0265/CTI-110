def miles_to_laps(user_miles):
    return user_miles / 0.25


if __name__ == '__main__':
    print("{:.2f}".format(miles_to_laps(float(input()))))