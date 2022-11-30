Feature: Sorting
    Scenario: Sort_abs with lambda
        Given List is [4, -30, 100, -100, 123, 1, 0, -1, -4]
        When Sorted this list with Sort_abs
        Then List is [123, 100, -100, -30, 4, -4, 1, -1, 0]
    