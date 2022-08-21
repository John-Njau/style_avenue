<template>
  <div>
    <div class="container px-4 py-5" id="hanging-icons">
      <h2 class="pb-1 border-bottom"></h2>
      <div class="row g-4 py-5 row-cols-1 row-cols-lg-3">
        <div class="col d-flex align-items-start">
          <div class="icon-square bg-light text-dark flex-shrink-0 me-3">
            <svg class="bi" width="1em" height="1em">
              <use xlink:href="#toggles2" />
            </svg>
          </div>
          <div>
            <h2 class="fw-bold" >Make Up</h2>
            <p>
              Paragraph of text beneath the heading to explain the heading.
              We'll add onto it with another sentence and probably just keep
              going until we run out of words.
            </p>
            <a href="#" class="btn btn-dark btn-sm"> Click </a>
          </div>
        </div>
        <div class="col d-flex align-items-start">
          <div class="icon-square bg-light text-dark flex-shrink-0 me-3">
            <svg class="bi" width="1em" height="1em">
              <use xlink:href="#cpu-fill" />
            </svg>
          </div>
          <div>
            <h2 class="fw-bold">Fragrance</h2>
            <p>
              Paragraph of text beneath the heading to explain the heading.
              We'll add onto it with another sentence and probably just keep
              going until we run out of words.
            </p>
            <a href="#" class="btn btn-dark btn-sm"> Click </a>
          </div>
        </div>
        <div class="col d-flex align-items-start">
          <div class="icon-square bg-light text-dark flex-shrink-0 me-3">
            <svg class="bi" width="1em" height="1em">
              <use xlink:href="#tools" />
            </svg>
          </div>
          <div>
            <h2 class="fw-bold">Hair</h2>
            <p>
              Paragraph of text beneath the heading to explain the heading.
              We'll add onto it with another sentence and probably just keep
              going until we run out of words.
            </p>
            <a href="#" class="btn btn-sm btn-dark"> Click </a>
          </div>
        </div>
      </div>
    </div>
    <h2 class="container pb-2 border-bottom"></h2>

    <div class="container col-xxl-8 px-4 py-5">
      <div class="row flex-lg-row-reverse align-items-center g-5 py-5">
        <div class="col-10 col-sm-8 col-lg-6">
          <img
            src="../assets/images/style_avenue_logo.jpg"
            class="m-auto d-sm-block d-none mx-lg-auto img-fluid"
            alt="Bootstrap Themes"
            width="700"
            height="500"
            loading="lazy"
          />
        </div>
        <div class="col-lg-6">
          <h1 class="display-6 fw-bold lh-1 mb-3">About us</h1>
          <p class="lead">
           We offer the best Make up services in the city. Our make up artists are medically sober, trained and accredited by the board.
          </p>
          <div class="d-grid gap-2 d-md-flex justify-content-md-start"></div>
        </div>
      </div>
    </div>
    <!-- map -->
    <section class="p-0">
        <div class="container">
            <div class="row g-4">
                
                      
                <div class="col-md">
                    <div id="map"></div>
                </div>
            </div>
        </div>
    </section>
  </div>
</template>

<script>
export default {
  mounted() {
    mapboxgl.accessToken =
      "pk.eyJ1Ijoiam9obnBvcHMiLCJhIjoiY2w2ejdob3V2MDFwczN1czJ2ZTdnZ3hocCJ9.Hlb3KWTbFjEo_KdB8TPNTA";
    var map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/mapbox/streets-v11",
      center: [-71.060982, 43.35725],
      zoom: 9,
    });
    map.addControl(new mapboxgl.NavigationControl());
  },
};
</script>

<style>
</style>