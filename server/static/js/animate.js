const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      const camera1 = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer({
          canvas: document.querySelector('#bg'),
          alpha: true, // 투명도 위해
      });
      const renderer1 = new THREE.WebGLRenderer({
          canvas: document.querySelector('#bg1'),
          alpha: true, // 투명도 위해
      });
      renderer.setPixelRatio(window.devicePixelRatio);
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setClearColor(0x000000, 0); // 투명도 위해
      renderer1.setPixelRatio(window.devicePixelRatio);
      renderer1.setSize(window.innerWidth, window.innerHeight);
      renderer1.setClearColor(0x000000, 0); // 투명도 위해
      camera.position.setZ(30);
      camera.position.setX(-3);
      camera1.position.setZ(30);
      camera1.position.setX(-3);
  
      // Initialize layers
      const layer1 = 0; // Default layer
      const layer2 = 1; // New layer for the second camera

      
  
      // 도형 추가
      const geometry = new THREE.TorusGeometry(10, 1, 16, 100);
      const material = new THREE.MeshStandardMaterial({ color: 0xEAEEFF });
      const torus = new THREE.Mesh(geometry, material);
      torus.layers.set(0);
      scene.add(torus); 
      
      // Add icosahedron on top left
      const cubeTexture = new THREE.TextureLoader().load('/static/image/main/favicon_logo.png');
      //top left
      const icosahedron1 = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), new THREE.MeshBasicMaterial({ map: cubeTexture }));
      icosahedron1.position.set(-40, 20, 0); // Adjust position as needed
      icosahedron1.layers.set(1);
      scene.add(icosahedron1); 

      // top right 
      const icosahedron2 = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), new THREE.MeshBasicMaterial({ map: cubeTexture }));
      icosahedron2.position.set(34, 20, 0); // Adjust position as needed
      icosahedron2.layers.set(1);
      scene.add(icosahedron2);


  
      // top left right
      const icosahedron3 = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), new THREE.MeshBasicMaterial({ map: cubeTexture }));
      icosahedron3.position.set(34, -15, 0); // Adjust position as needed
      icosahedron3.layers.set(1);
      scene.add(icosahedron3);

      //top left
      const icosahedron4 = new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), new THREE.MeshBasicMaterial({ map: cubeTexture }));
      icosahedron4.position.set(-40, -15, 0); // Adjust position as needed
      icosahedron4.layers.set(1);
      scene.add(icosahedron4); 

      

 

      
  
      // 라이트
      const pointLight = new THREE.PointLight(0xffffff); // 안쪽 빛
      pointLight.position.set(5, 5, 5);
      const ambientLight = new THREE.AmbientLight(0xffffff);
      scene.add( pointLight,ambientLight);
  
      camera.layers.enable(0);
      camera1.layers.disableAll();
      camera1.layers.enable(1);
      // Scroll Animation
      function moveCamera() {
          const t = document.body.getBoundingClientRect().top;
          camera.position.z = t * -0.01;
          camera.position.x = t * -0.0002;
          camera.rotation.y = t * -0.0002;
      }
  
      document.body.onscroll = moveCamera;
      moveCamera();
      // Animation Loop
  
      function animate() {
          requestAnimationFrame(animate);
          torus.rotation.x += 0.01;
          torus.rotation.y += 0.005;
          torus.rotation.z += 0.01;
          icosahedron1.rotation.x += 0.01;
          icosahedron1.rotation.y += 0.01;
          icosahedron2.rotation.x += 0.01;
          icosahedron2.rotation.y += 0.01;
          icosahedron3.rotation.x += 0.01;
          icosahedron3.rotation.y += 0.01;
          icosahedron4.rotation.x += 0.01;
          icosahedron4.rotation.y += 0.01;
          renderer.render(scene, camera);
          renderer1.render(scene, camera1);
      }
      animate();