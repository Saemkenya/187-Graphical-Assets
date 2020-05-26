$(function () {
  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  );
  var renderer = new THREE.WebGLRenderer();

  renderer.setClearColor(0x000000);
  renderer.setSize(window.innerWidth, window.innerHeight);

  var axis = new THREE.AxesHelper(10);
  scene.add(axis);

  var cubeGeometry = new THREE.BoxGeometry(5, 5, 5);
  var cubeMaterial = new THREE.MeshBasicMaterial({
    color: 0xff0000,
    // wireframe: true,
  });
  var cube = new THREE.Mesh(cubeGeometry, cubeMaterial);

  cube.position.x = 0;
  cube.position.y = 0;
  cube.position.z = 0;

  scene.add(cube);

  camera.position.x = 10;
  camera.position.y = 10;
  camera.position.z = 10;

  camera.lookAt(scene.position);

  //   renderer.render(scene, camera);

  var animate = function () {
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    cube.rotation.z += 0.01;
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  };

  animate();

  $("#webGL-container").append(renderer.domElement);
});
