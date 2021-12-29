var rules = '2';
var document = {};
function getRules(){return rules}
document.createElement = function() {
     return {
             sheet: {
                     insertRule: function(rule, i) {
                             if (rules.length == 0) {
                                     rules = rule;
                             } else {
                                     rules = rules + '#' + rule;
                             }
                     }
             }
     }
};

document.write(rules)