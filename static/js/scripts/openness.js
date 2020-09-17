function openness(id, d){
    var str = num_string(d)
    ctx = document.getElementById(id).getContext("2d");
    myChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: [1, 2],
        datasets: [{
          label: "Emails",
          pointRadius: 0,
          pointHoverRadius: 0,
          backgroundColor: ['#f17e5d', '#f4f3ef'],
          borderWidth: 0,
          data: [d, 1-d]
        }]
      },
      options: {
        elements: {
          center: {
            text: str,
            color: '#66615c', // Default is #000000
            fontStyle: 'Arial', // Default is Arial
            sidePadding: 60 // Defualt is 20 (as a percentage)
          }
        },
        cutoutPercentage: 90,
        legend: {

          display: false
        },

        tooltips: {
          enabled: false
        },

        scales: {
          yAxes: [{

            ticks: {
              display: false
            },
            gridLines: {
              drawBorder: false,
              zeroLineColor: "transparent",
              color: 'rgba(255,255,255,0.05)'
            }

          }],

          xAxes: [{
            barPercentage: 1.6,
            gridLines: {
              drawBorder: false,
              color: 'rgba(255,255,255,0.1)',
              zeroLineColor: "transparent"
            },
            ticks: {
              display: false,
            }
          }]
        },
      }
    });
  }