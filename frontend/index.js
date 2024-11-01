var modal = document.getElementById("myModal");
var btn = document.getElementById("create");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
  modal.style.display = "block";
  
  setTimeout(() => {
    modal.style.opacity = "1";
    document.querySelector(".modal-content").style.opacity = "1";
    document.querySelector(".modal-content").style.transform = "scale(1)";
  }, 10);
}

span.onclick = function() {
  modal.style.opacity = "0";
  document.querySelector(".modal-content").style.opacity = "0";
  document.querySelector(".modal-content").style.transform = "scale(0.9)";
    setTimeout(() => {
    modal.style.display = "none";
  }, 500);
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.opacity = "0";
    document.querySelector(".modal-content").style.opacity = "0";
    document.querySelector(".modal-content").style.transform = "scale(0.9)";
    
    setTimeout(() => {
      modal.style.display = "none";
    }, 500);
  }
}

const checkboxes = document.querySelectorAll('.task-checkbox');

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const taskContent = this.parentNode.querySelector('.task-content');
        if (this.checked) {
            taskContent.classList.add('task-completed');
        } else {
            taskContent.classList.remove('task-completed');
        }
    });
});
