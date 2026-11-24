"""Monday, Reviewed in One Line.

A review has a verdict, a star rating, and a list of grievances. Monday
earns the lowest possible score and still shows up next week, uninvited,
like a subscription nobody remembers signing up for -- and the one-star
review changes nothing, because Monday never reads its reviews.
"""

# One star, three grievances, zero chance of a refund on the weekend.
REVIEW = "Monday: one star. Arrived uninvited, stole my weekend, and the coffee machine was already broken when it got here."


def main() -> None:
    print(REVIEW)


if __name__ == "__main__":
    main()
