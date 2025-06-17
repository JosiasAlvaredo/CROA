const { createApp } = Vue

  createApp({
  data() {
    return {
      url: "http://127.0.0.1:5000/equipos_registro",
      equipos: [],
      error: false,
      cargando: true,

      nuevoEquipo: {
        nombre: '',
        categoria: '',
        deporte: '',
        puntaje: 0
      },
      nuevoInvitado: {
        id_equipo: '',
        dni: 0,
        nombre_apellido: '',
        dieta: ''
      }

    };
  },
  created() {
    this.fetchData(this.url);
  },
  methods: {
    fetchData(url) {
      fetch(url)
        .then(response => response.json())
        .then(data => {
          console.log("Datos recibidos:", data);
          this.equipos = data;
          this.cargando = false;
        })
        .catch(err => {
            console.error(err);
            this.error = true;
            this.cargando = false;
        });
    },
    agregarEquipo() {
      fetch('http://localhost:5000/nuevo_equipo', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.nuevoEquipo)
      })
      .then(res => res.json())
      .then(() => {
        alert("Equipo agregado");
        this.nuevoEquipo = { nombre: '', categoria: '', deporte: '', puntaje: 0 };
        this.fetchData(); // recargar equipos
      })
      .catch(err => console.error(err));
    },

    agregarInvitado() {
      fetch('http://localhost:5000/nuevo_invitado', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.nuevoInvitado)
      })
      .then(res => res.json())
      .then(() => {
        alert("Invitado agregado");
        this.nuevoInvitado = { id_equipo: '', dni: 0, nombre_apellido: '', dieta: '' };
        this.fetchData(); // recargar equipos con invitados
      })
      .catch(err => console.error(err));
    },
    mounted() {
      this.fetchData();  // Cargar equipos al iniciar
    }
  }
}).mount('#app');