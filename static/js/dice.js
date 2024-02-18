const diceScene = new THREE.Scene();
const diceCamera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const diceRenderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('.dice3D'),
    alpha: true, // 투명도 위해
});

      diceRenderer.setPixelRatio(window.devicePixelRatio);
      diceRenderer.setSize(window.innerWidth, window.innerHeight);
      diceRenderer.setClearColor(0x000000, 0); // 투명도 위해

      diceCamera.position.setZ(30);
      diceCamera.position.setX(-3);

      
  
      // 도형 추가
      
      
      // Add icosahedron on top left
      const cubeTexture = new THREE.TextureLoader().load('/static/image/main/favicon_logo.png');
      //top left
      const icosahedron1 = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), new THREE.MeshBasicMaterial({ map: cubeTexture }));
      icosahedron1.position.set(-40, 20, 0); // Adjust position as needed
      diceScene.add(icosahedron1); 

      // top right 
      const icosahedron2 = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), new THREE.MeshBasicMaterial({ map: cubeTexture }));
      icosahedron2.position.set(34, 20, 0); // Adjust position as needed
      diceScene.add(icosahedron2);


  
      // top left right
      const icosahedron3 = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), new THREE.MeshBasicMaterial({ map: cubeTexture }));
      icosahedron3.position.set(34, -15, 0); // Adjust position as needed
      diceScene.add(icosahedron3);

      //top left
      const icosahedron4 = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), new THREE.MeshBasicMaterial({ map: cubeTexture }));
      icosahedron4.position.set(-40, -15, 0); // Adjust position as needed
      diceScene.add(icosahedron4); 

      

 

      
  
      // 라이트
      const dicePointLight = new THREE.PointLight(0xffffff); // 안쪽 빛
      dicePointLight.position.set(5, 5, 5);
      const diceAmbientLight = new THREE.AmbientLight(0xffffff);
      diceScene.add( dicePointLight,diceAmbientLight);

      // Resize Handler
    function onWindowResize() {
        // Update camera aspect ratios to match new window size
        diceCamera.aspect = window.innerWidth / window.innerHeight;
        diceCamera.updateProjectionMatrix();

        // Adjust renderer sizes
        diceRenderer.setSize(window.innerWidth, window.innerHeight);
    }

    // Listen for window resize events
    window.addEventListener('resize', onWindowResize, false);

    // Call resize handler once to set initial sizes
    onWindowResize();
      
      // Animation Loop
  
      function animate() {
          requestAnimationFrame(animate);
          icosahedron1.rotation.x += 0.01;
          icosahedron1.rotation.y += 0.01;
          icosahedron2.rotation.x += 0.01;
          icosahedron2.rotation.y += 0.01;
          icosahedron3.rotation.x += 0.01;
          icosahedron3.rotation.y += 0.01;
          icosahedron4.rotation.x += 0.01;
          icosahedron4.rotation.y += 0.01;
          diceRenderer.render(diceScene, diceCamera);
      }
      animate();