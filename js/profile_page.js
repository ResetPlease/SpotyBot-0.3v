var current_id = 2;

function replaceName(id_btn){
    var elem = document.getElementById("ToUserName");
    elem.innerText = id_btn;
}
function SendBot(btn_id)
{ 
    $.ajax({
        url: '/addbot',
        data: $(`#${btn_id}_form`).serialize(),
        type: 'POST',
        success: function(response){
            if(response == 'Error'){
                alert('Wrong username');
                return;
            }
            else{
                console.log(`#${btn_id}_login`);
                $(`#${btn_id}_login`).replaceWith(document.getElementById(`${btn_id}_login`).value);
                $(`#${btn_id}_passw`).replaceWith(document.getElementById(`${btn_id}_passw`).value);
                $(`#${btn_id}_first`).replaceWith(document.getElementById(`${btn_id}_first`).value);
                $(`#${btn_id}_second`).replaceWith(document.getElementById(`${btn_id}_second`).value);
                $(`#${btn_id}_lim`).replaceWith(document.getElementById(`${btn_id}_lim`).value);
                document.getElementById(`${btn_id}`).remove();
            }
        },
        error: function(error) {
            console.log(error);
            return;
        }
    });
}
function DrawBotPlace(){
    var ins = `<form id="${current_id}_form" method="post">
    <li class="list-group-item d-block">
        <div class="row align-items-center">
            <div class="col-12 col-sm-5 col-lg-10 text-center text-sm-left">
                <h6 id="myModalLabel">Логин: 
                    <input style="background-color:#404040;color: white;" id="${current_id}_login" name="login" autocomplete="off" class=" form-control-sm border-0 font-weight-light rounded-pill" type="text"  placeholder="login"></h6> 
                <h6 id="myModalLabel">Пароль:
                    <input style="background-color:#404040;color:white;" id="${current_id}_passw" name="password" autocomplete="off" class=" form-control-sm border-0 font-weight-light rounded-pill" type="text"  placeholder="password"></h6>
                <h6 id="myModalLabel">Примерное время работы: с
                    <input style="background-color:#404040;color: white;" id="${current_id}_first" name="first_t" autocomplete="off" class=" form-control-sm border-0 font-weight-light rounded-pill" type="time"  placeholder="enter link...">  до 
                    <input style="background-color:#404040;color:white;" id="${current_id}_second" name="second_t" autocomplete="off" class=" form-control-sm border-0 font-weight-light rounded-pill" type="time"  placeholder="enter link..."></h6>
                <h6 id="myModalLabel">Ограничение по прослушиваниям: <input style="background-color:#404040; color:white;" id="${current_id}_lim" name="listen" autocomplete="off" class=" form-control-sm border-0 font-weight-light rounded-pill" type="text" placeholder="day:week:month"></h6>
                <h6 id="myModalLabel" class="${current_id}_chekH6"><input style="margin:auto;" id="${current_id}_check" name="listenCheck" onclick="DrIm(this.id)" type="checkbox"> Переключатель  
                <div id="${current_id}_div" style="display:none"><br>Диапазон с <input style="background-color:#404040; color:white;"
        id="${current_id}_beginT" name="beginT" autocomplete="off" class="form-control-sm border-0 font-weight-light rounded-pill" type="text"> до 
        <input style="background-color:#404040; color:white;" id="${current_id}_endT" name="endT" autocomplete="off" class="form-control-sm border-0 font-weight-light rounded-pill" type="text"></div></h6><br>
                    <button style="width: 100px;"class="btn btn-outline-primary float-right" type="button" id="${current_id}" onclick="SendBot(this.id);">Start</button>
            </div>
        </div>
    </li>
    </form>`;
    document.getElementById("contact-list").innerHTML += ins;
    current_id += 1;
}

function DrIm(chbId){
    element = document.getElementById(chbId);
    if(element.checked == true){
        document.getElementById(chbId.split("_")[0]+"_div").style.display = "block";
    }
    else{
        document.getElementById(chbId.split("_")[0]+"_div").style.display = "none";
    }
}


