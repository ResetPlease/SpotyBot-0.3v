var current_id = 2;
function DrawSetUpPlace(){
    var ins = `<form id="${current_id}_form" method="post">
    <li class="list-group-item d-block">
        <div class="row align-items-center">
            <div class="col-12 col-sm-5 col-lg-10 text-center text-sm-left">
            <h6 id="myModalLabel">Ссылка на альбом/артиста: 
            <input style="background-color:#404040; color:white; width: 300px;" id="${current_id}_link" name="link" autocomplete="off" class=" form-control-sm border-0 font-weight-light rounded-pill" type="text"  placeholder="enter link..."></h6>
                <h6 id="myModalLabel">Ограничение по прослушиваниям: <input style="background-color:#404040; color:white;" id="${current_id}_lim" name="listen" autocomplete="off" class=" form-control-sm border-0 font-weight-light rounded-pill" type="text" placeholder="day:week:month"></h6>
                    <button style="width: 100px;"class="btn btn-outline-primary float-right" type="button" id="${current_id}" onclick="SendSetup(this.id);">Commit</button>
            </div>
        </div>
    </li>
    </form>`;
    document.getElementById("contact-list").innerHTML += ins;
    current_id += 1;
}
function SendSetup(btn_id)
    { 
        $.ajax({
            url: '/addSetUp',
            data: $(`#${btn_id}_form`).serialize(),
            type: 'POST',
            success: function(response){
                if(response == 'Error'){
                    alert('Something is wrong...');
                    return;
                }
                else{
                    $(`#${btn_id}_lim`).replaceWith(document.getElementById(`${btn_id}_lim`).value);
                    $(`#${btn_id}_link`).replaceWith(document.getElementById(`${btn_id}_link`).value);
                    document.getElementById(`${btn_id}`).remove();
                }
            },
            error: function(error) {
                console.log(error);
                return;
            }
        });
}