function del_file(file_name,file_count,page_name){
			var check = confirm(file_name+" 파일을 삭제하시겠습니까?");
	      	  /* if(check == true) else false */
	      	if(check){ 
	      		location.href="/sle/wiki/delete/"+page_name+"/"+file_count;
	      	}
	      	else{
				
	      	}
}
$(document).ready(function(){
		var input= $('#id_file');
		$("#id_file").on("change",function(){
			if(this.files[0].size <=  30000000 ){
					$("#upload_file_name").val(this.files[0].name);
					
			}else{
					alert("최대 30Mb의 파일만 업로드 할 수 있습니다.");
					input.replaceWith(input = input.clone(true));
					$("#upload_file_name").val("");
			}
			
		});
		$("#file_upload").on("submit",function(){
			if($("#upload_file_name").val() != "" && $("#id_file").val() != ""){
				return true;
			}else{
				alert("업로드 할 파일을 선택해주세요.");
				return false;
			}
		})
});