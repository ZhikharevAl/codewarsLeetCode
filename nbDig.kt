/*
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Implement the function taking n and d as parameters and returning this count.
*/

fun nbDig(n: Int, d: Int): Int {
    var count = 0

    for (k in 0..n) {
        val square = k * k
        count += digitCount(square, d)
    }

    return count
}

fun digitCount(number: Int, digit: Int): Int {
    var count = 0
    var num = number

    while (num != 0) {
        val lastDigit = num % 10
        if (lastDigit == digit) {
            count++
        }
        num /= 10
    }

    return count
}
