def test_rectangle():
    rect1 = Rectangle()
    rect2 = Rectangle()
    
    # Test that the objects were created correctly
    assert rect1 is not None
    assert rect2 is not None
    
    # Test that the objects are distinct
    assert rect1 is not rect2
    
    # Test that the objects are instances of the Rectangle class
    assert isinstance(rect1, Rectangle)
    assert isinstance(rect2, Rectangle)
test_rectangle()
