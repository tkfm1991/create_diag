function init(){
    $(function(){
        console.log('read jQuery File!');
    });
}

function line_hover(){
    $(".line").hover(
        function() {
            document.getElementById("area1").innerText = $(this).attr("id");
            console.log('in');
        },
        function() {
            document.getElementById("area1").innerText = 'default message';
            console.log("out");
        }
    )    
}

// function mouseover(){
//     document.getElementById("area1").innerText = "マウスポインタ1が当たっています。";
//     // console.log( $(this).attr("id") );
    
// }
// function mouseout(){
//     document.getElementById("area1").innerText = "ここにマウスポインタを当ててください。";
//     // console.log( "out" );
// }


init();
line_hover();

