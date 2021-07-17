<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>My first chart</title>
  </head>
  <body>
    <h1>My first chart</h1>

   <!-- <nav class="navbar navbar-expand-lg bg-dark navbar-dark"></nav> -->

    <div class="col-8 offset-2 my-5">
        <div class="card">
            <div class="card-body">
                <h5>ez itt az</h5>
                <hr>
                <canvas id="myChart" width="100" height="40"></canvas>
            </div>
            <div>
              <table id="tab" style="width:100%">
                <tr id = "tt">
                  <th>town</th>
                  <th>nr</th>
                </tr>
                <!-- <tr id="t2">
                  <td id= "t2-1">ss</td>
                  <td id= "t2-2">eee</td>
                </tr>
                <tr id="t3">
                  <td id= "t3-1">ss</td>
                  <td id= "t3-2">eee</td>
                </tr> -->

              </table>

            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script>
    function fetchit() {
            fetch('/getdata/')
                .then(res => res.json())
                .then(res => {
                firstar = []
                secondar = []

                // for ( var k  in res )
                //       { console.log(k)}

                Object.keys(res).forEach(val  => firstar.push(val) )
                Object.values(res).forEach(val  => secondar.push(val) )
              

                table1 = document.getElementById('mt')
                )

                if (table1) {  
                    for (let x = 0; x < firstar.length; x++ ){

                    const newt2 = document.getElementById('tab')
                    newt2.innerHTML = `<tr>
                                      <th>town</th>
                                      <th>nr</th>
                                      </tr>
                                      <tr>
                                      <td id= "t2-1"></td>
                                      <td id= "t2-2"></td>
                                      </tr>`
                    // document.getElementById('tab').appendChild(newt2) 
                                    
                  
                    for (let x = 0; x < firstar.length; x++ ){

                        const newt2 = document.createElement('tr')
                        newt2.setAttribute('id', 'mt')
                        newt2.innerHTML = `<tr id="mt">
                                          <td id= "t2-1">${firstar[x]}</td>
                                          <td id= "t2-2">${secondar[x]}</td>
                                          </tr>`
                        document.getElementById('tab').appendChild(newt2)
                        

                    }
                
                }  

              } else {
                for (let x = 0; x < firstar.length; x++ ){

                    const newt2 = document.createElement('tr')
                    newt2.setAttribute('id', 'mt')
                    newt2.innerHTML = `<tr id="mt">
                                      <td id= "t2-1">${firstar[x]}</td>
                                      <td id= "t2-2">${secondar[x]}</td>
                                      </tr>`
                    document.getElementById('tab').appendChild(newt2)
                    

}


              }
              
            })}

    setInterval(fetchit, 10000)

    // function thisIS(){
    //   const mt = document.getElementById('mt')
    //     if (1){
    //       document.getElementById('tab').innerHTML = ''
    //       fetchit()

    //     }
    // }
  
    
    fetchit()
    // setInterval(thisIS, 1000) 
    

    

    </script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>


  </body>
</html>

