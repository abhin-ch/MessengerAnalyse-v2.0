var word_count = data['word_count_percent'];
var a_name = Object.keys(word_count);
var a_data = Object.values(word_count) ;
var ctx = document.getElementById('word_sent').getContext('2d');
var chart = new Chart(ctx, {
type: 'doughnut',
data: {
    labels: a_name,
    datasets: [{
    label: "Message Sent",
    backgroundColor: list_name_colour,
    data: a_data
    }]
},
options: {}
});