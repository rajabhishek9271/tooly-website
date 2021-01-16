// --------EXPERIENCE------------
// > 5 years

var experience;
$("#experience-cbx").change(function() {
  experience = ">5";
  experienceAJAX();
});

// 3-5

$("#experience-cbx-two").change(function() {
experience = "3-5";
experienceAJAX();
});

// 1-3
$("#experience-cbx-three").change(function() {
experience = "1-3";
experienceAJAX();
});

// >1
$("#experience-cbx-four").change(function() {
experience = ">1";
experienceAJAX();
});

function experienceAJAX(){
  $.ajax({
    type:"get",
    url: "http://127.0.0.1:8000/recruiter/jobs_list/",
    data:{
      exp:experience
    },
    success: function(response){
      var ids = response.ids;
      var total_ids = response.total_ids;

      for(var i=0;i<total_ids.length;i++){
        var currr = '#'+(total_ids[i]);
        $(currr).css('display', 'none');

      }
      for(var i=0;i<ids.length;i++){
        var currr = '#'+(ids[i]);
        $(currr).css('display', 'inherit');
      }
    },

  });
}
