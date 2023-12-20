// Test cases:
// 1. Testing when x1, y1, x2, y2 all have the same values.
// 2. Testing when x1, y1, x2, y2 are all positive values.
// 3. Testing when x1, y1, x2, y2 are all negative values.
// 4. Testing when x1, y1, x2, y2 are all zero values.

func TestMain(t *testing.T) {
	// Test case 1
	x1, y1, x2, y2 := 0, 0, 0, 0
	expected := 0.0
	result := calculateDistance(x1, y1, x2, y2)
	if result != expected {
		t.Errorf("Expected %f, but got %f", expected, result)
	}

	// Test case 2
	x1, y1, x2, y2 = 3, 4, 5, 6
	expected = 2.8284271247461903
	result = calculateDistance(x1, y1, x2, y2)
	if result != expected {
		t.Errorf("Expected %f, but got %f", expected, result)
	}

	// Test case 3
	x1, y1, x2, y2 = -3, -4, -5, -6
	expected = 2.8284271247461903
	result = calculateDistance(x1, y1, x2, y2)
	if result != expected {
		t.Errorf("Expected %f, but got %f", expected, result)
	}

	// Test case 4
	x1, y1, x2, y2 = 0, 0, 0, 0
	expected = 0.0
	result = calculateDistance(x1, y1, x2, y2)
	if result != expected {
		t.Errorf("Expected %f, but got %f", expected, result)
	}
}

func calculateDistance(x1, y1, x2, y2 int) float64 {
	return math.Sqrt(math.Pow(float64(x1-x2), 2) + math.Pow(float64(y1-y2), 2))
}
