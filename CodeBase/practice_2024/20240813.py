


"""
 Instructions to candidate.
  1) Given an array of non-negative integers representing the elevations
     from the vertical cross section of a range of hills, determine how
     many units of snow could be captured between the hills.

     See the example array and elevation map below.
                                 ___
             ___                |   |        ___
            |   |        ___    |   |___    |   |
         ___|   |    ___|   |   |   |   |   |   |
     ___|___|___|___|___|___|___|___|___|___|___|___
     [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]
                                 ___
             ___                |   |        ___
            |   | *   *  _*_  * |   |_*_  * |   |
         ___|   | *  _*_|   | * |   |   | * |   |
     ___|___|___|_*_|___|___|_*_|___|___|_*_|___|___
     [0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0]

     Solution: In this example 13 units of snow (*) could be captured.

  2) Implement computeSnowpack() correctly.
  3) Consider adding some additional tests in doTestsPass().
"""