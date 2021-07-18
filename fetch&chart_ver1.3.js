chartExists = false
function fetchit() {
      fetch('/getdata/')
          .then(res => res.json())
          .then(res => {
          towns = []
          heights= []


          if (chartExists != false) {chartExists = true}
          else {chartExists == false}

          Object.keys(res).forEach(val  => towns.push(val) )
          Object.values(res).forEach(val  => heights.push(val) )

          function chartMain() {
              function updateChart(chart) {
                                  chart.data.labels = towns
                                  chart.data.datasets[0].data = heights
                                  chart.update()
                                  console.log('chart is updated')
                              }


            var ctx = document.getElementById('myChart').getContext('2d');
            if (chartExists == false) {
            console.log('chart created')
            chartExists = true
                chartOne = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: towns,

                        datasets: [{
                            label: 'heights in these towns',
                            data: heights,
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',


                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',

                            ],
                            borderWidth: 1
                        }]
                    },
                    options: { scales: {  y: { beginAtZero: true }, animation: false,},
                    }


                   }



                  ) }

                  else {
                      updateChart(chartOne)

                                 }
                     }
                  chartMain()

              })} 

  fetchit()
  setInterval(fetchit, 10000)
