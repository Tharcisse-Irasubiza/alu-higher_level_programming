
#!/bin/bash

# Task 0: Empty Rectangle
cat > 0-rectangle.js <<'EOF'
#!/usr/bin/node
class Rectangle {}

module.exports = Rectangle;
EOF

# Task 1: Rectangle with width and height
cat > 1-rectangle.js <<'EOF'
#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
EOF

# Task 2: Validate width and height
cat > 2-rectangle.js <<'EOF'
#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (!Number.isInteger(w) || w <= 0 ||
        !Number.isInteger(h) || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
EOF

# Task 3: Print rectangle
cat > 3-rectangle.js <<'EOF'
#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (!Number.isInteger(w) || w <= 0 ||
        !Number.isInteger(h) || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
EOF

# Task 4: Rotate and double rectangle
cat > 4-rectangle.js <<'EOF'
#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (!Number.isInteger(w) || w <= 0 ||
        !Number.isInteger(h) || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
EOF

# Task 5: Square extends Rectangle
cat > 5-square.js <<'EOF'
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
}

module.exports = Square;
EOF

# Task 6: Square with custom print character
cat > 6-square.js <<'EOF'
#!/usr/bin/node
const PreviousSquare = require('./5-square');

class Square extends PreviousSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
EOF

# Task 7: Count occurrences
cat > 7-occurrences.js <<'EOF'
#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter((element) => element === searchElement).length;
};
EOF

# Task 8: Reverse a list without reverse()
cat > 8-esrever.js <<'EOF'
#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduce((result, element) => {
    result.unshift(element);
    return result;
  }, []);
};
EOF

# Task 9: Log arguments with a counter
cat > 9-logme.js <<'EOF'
#!/usr/bin/node
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
EOF

# Task 10: Convert a number to another base
cat > 10-converter.js <<'EOF'
#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
EOF

echo "Successfully created all 11 JavaScript files!"

