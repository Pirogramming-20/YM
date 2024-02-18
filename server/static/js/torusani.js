const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('.torus'),
    alpha: true, // 투명도 위해
});

      renderer.setPixelRatio(window.devicePixelRatio);
      renderer.setSize(window.innerWidth, window.innerHeight);
      renderer.setClearColor(0x000000, 0); // 투명도 위해

      camera.position.setZ(30);
      camera.position.setX(-3);
  


      
  
      // 도형 추가
      const geometry = new THREE.TorusGeometry(10, 1, 16, 100);
      const material = new THREE.MeshStandardMaterial({ color: 0xEAEEFF });
      const torus = new THREE.Mesh(geometry, material);
      scene.add(torus); 
      
      // 라이트
      const pointLight = new THREE.PointLight(0xffffff); // 안쪽 빛
      pointLight.position.set(5, 5, 5);
      const ambientLight = new THREE.AmbientLight(0xffffff);
      scene.add( pointLight,ambientLight);
  

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
          renderer.render(scene, camera);
      }
      animate();