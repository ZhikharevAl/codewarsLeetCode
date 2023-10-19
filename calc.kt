
fun main(args: Array<String>) {
    println("Enter the first number:")
    val a = readlnOrNull()?.toIntOrNull()

    println("Enter the second number:")
    val b = readlnOrNull()?.toIntOrNull()

    println("Enter operation (plus, minus, multiply, or divide):")
    val opp = readlnOrNull()

    val result = operator(opp, a, b)

    println("Result: $result")
}

fun operator(opp: String?, a: Int?, b: Int?): Int {
    if (a == null || b == null) {
        println("Invalid input. Please enter valid integers.")
        return 0
    }

    return when (opp) {
        "plus" -> a + b
        "minus" -> a - b
        "multiply" -> a * b
        "divide" -> {
            if (b != 0) {
                a / b
            } else {
                println("Division by zero is not allowed.")
                return 0
            }
        }
        else -> {
            println("Invalid operation. Please enter 'plus', 'minus', 'multiply', or 'divide'.")
            return 0
        }
    }
}
