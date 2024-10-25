// function previewImage(event) {
//        const currentImage = document.getElementById('current-profile-image');
//        const newProfileImage = document.getElementById('new-profile-image');
       
//        // Si hay un archivo seleccionado
//        if (event.target.files.length > 0) {
//            const file = event.target.files[0];
//            const reader = new FileReader();
   
//            // Mostrar la imagen cargada
//            reader.onload = function(e) {
//                newProfileImage.src = e.target.result;
//                newProfileImage.style.display = 'block';  // Mostrar la imagen de vista previa
//                currentImage.style.display = 'none';  // Ocultar la imagen actual
//            }
   
//            reader.readAsDataURL(file);
//        } else {
//            // Si no hay archivo seleccionado, mostrar la imagen actual
//            newProfileImage.style.display = 'none';  // Ocultar la nueva imagen
//            currentImage.style.display = 'block';  // Mostrar la imagen actual
//        }
//    }
   