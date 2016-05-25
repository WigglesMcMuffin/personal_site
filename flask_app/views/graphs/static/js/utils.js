var thing = '';
var other_thing = '';

var get_attr = R.curry(function(value, object) {
  return object[value];
})

var get_attrs = function(list_of_objects) {
  //assuming objects are homogoneous
  return Object.keys(list_of_objects);
}
