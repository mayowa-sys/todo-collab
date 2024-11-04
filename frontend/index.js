// Select elements
const modal = document.getElementById("myModal");
const updateModal = document.getElementById("updateModal");
const createButton = document.getElementById("create");
const closeButton = document.getElementsByClassName("close")[0];
const updateCloseButton = updateModal.querySelector(".close");

// Open the 'Add New Task' modal
createButton.onclick = function () {
    modal.style.display = "block";
    setTimeout(() => {
        modal.style.opacity = "1";
        document.querySelector(".modal-content").style.opacity = "1";
        document.querySelector(".modal-content").style.transform = "scale(1)";
    }, 10);
}

// Close the 'Add New Task' modal
closeButton.onclick = function () {
    closeForm();
}

// Close modals when clicking outside
window.onclick = function (event) {
    if (event.target == modal || event.target == updateModal) {
        closeForm();
        closeUpdateForm();
    }
}

// Close 'Add New Task' modal function
function closeForm() {
    modal.style.opacity = "0";
    document.querySelector(".modal-content").style.opacity = "0";
    document.querySelector(".modal-content").style.transform = "scale(0.9)";
    setTimeout(() => { modal.style.display = "none"; }, 500);
}

// Open the 'Update Task' modal with task data
function openUpdateForm(taskTitle, taskDesc, taskDate) {
    updateModal.style.display = "block";
    document.getElementById("update-title").value = taskTitle;
    document.getElementById("update-description").value = taskDesc;
    document.getElementById("update-date").value = taskDate;

    setTimeout(() => {
        updateModal.style.opacity = "1";
        updateModal.querySelector(".modal-content").style.opacity = "1";
        updateModal.querySelector(".modal-content").style.transform = "scale(1)";
    }, 10);
}

// Close the 'Update Task' modal function
function closeUpdateForm() {
    updateModal.style.opacity = "0";
    updateModal.querySelector(".modal-content").style.opacity = "0";
    updateModal.querySelector(".modal-content").style.transform = "scale(0.9)";
    setTimeout(() => { updateModal.style.display = "none"; }, 500);
}

// Add event listeners for 'Update' buttons
document.querySelectorAll('.update-button').forEach(button => {
    button.onclick = function () {
        const task = button.closest('.task');
        const taskTitle = task.querySelector('.task-title').textContent;
        const taskDesc = task.querySelector('.task-desc').textContent;
        const taskDate = task.querySelector('.task-date span').textContent;
        
        openUpdateForm(taskTitle, taskDesc, taskDate);
    };
});

// Handle update form submission
document.getElementById('updateForm').onsubmit = function(event) {
    event.preventDefault();
    // Logic to update the task with new values
    closeUpdateForm();
};


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

function openTask(evt, taskName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(taskName).style.display = "block";
  evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();