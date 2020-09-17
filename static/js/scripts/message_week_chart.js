console.log(data);
var msg_by_week = data['message_by_day_week_g'];
var c_name = Object.keys(msg_by_week);
var c_data = Object.values(msg_by_week);
var ctx = document.getElementById('week_chart').getContext('2d');
var lab = [];
for (var i = 0; i < c_name.length; i++) {
    console.log(list_name_colour)
    console.log("This is the color of i")
    console.log(list_name_colour[i])
    dict = {label:c_name[i], order:1 ,borderColor: list_name_colour[i],backgroundColor: list_name_colour[i] ,fill:false ,data:c_data[i]};
    lab.push(dict);
}
console.log(lab);
var chart = new Chart(ctx, {
    // The type of chart 
    type: 'line',
    // The data for the dataset
    data: {
        labels: ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",],
        datasets: lab
    },
    options: {scales: {xAxes: [{gridLines: {drawOnChartArea: false}}],
                        yAxes: [{gridLines: {drawOnChartArea: false}, display:false}
                            
                        ]}}});
                        