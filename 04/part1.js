const fs = require('fs');
const R = require('ramda')

// String -> Boolean
const isSixDigits = R.propEq('length', 6);

// Any -> Boolean
const toBool = x => !!x

// StringOfDigits -> Boolean
const digitsNeverDecrease = R.pipe(
  R.reduce(
    (biggest, curr) => biggest > Number(curr) ? R.reduced(false) : Number(curr),
    0
  ),
  toBool
);

// [ [Any, Any]* ] -> Boolean
const hasPairWhereBothEqual = R.any(R.apply(R.equals))

// String -> String[] | ('ABC' -> [ ['A', 'B'], ['B', 'C'], ['C', 'D'] ])
const convertStringToOverlappingPairs = R.aperture(2);

// String -> Boolean
const hasTwoAdjacentDigits = R.pipe(
  convertStringToOverlappingPairs,
  hasPairWhereBothEqual
)

// String -> Boolean
const allRulesPass = R.allPass([digitsNeverDecrease, hasTwoAdjacentDigits, isSixDigits])
const filterValidInputs = R.filter(allRulesPass);

// ([Number, Number]) -> String[]
const buildArray = ([min, max]) =>
  R.unfold(
    n => n > max ? false : [String(n), n+1]
  )(min)


module.exports = R.pipe(
  fs.readFileSync,
  R.invoker(0, 'toString'),
  R.split('-'),
  R.map(Number),
  buildArray,
  filterValidInputs,
  R.prop('length'),
  console.log
)

// node part1.js input
module.exports(process.argv[2])
// prints 1154