<template>
  <div class="hello">
    <!-- <div class="options m-0 p-0">
      <ul>
        <li>Face Beat</li>
        <li>Fragrance</li>
        <li>Hair</li>
        <li>Book</li>
      </ul>
    </div> -->
    <div></div>
    <div class="container mt-2">
      <div class="to-flex">
          <div v-for="category in categories" :key="category.id">
          <div class="grid">
            <div class="g-col-lg-4 g-col-md-3 card mx-2">
              <div class="card-body">
                <img :src="category.pic" alt="photo" class="pic image-fluid" />
                <h5 class="card-title">{{ category.name }}</h5>
                <p class="card-text">{{ category.description }}</p>
                <p class="card-text">
                  Some quick example text to build on the card title and make up
                  the bulk of the card's content.
                </p>
                <a href="#" class="btn btn-sm btn-light">This category</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
  props: {
    msg: String,
  },
  data() {
    return {
      title: "Style Avenue Studio",
    };
  },
  computed: {
    categories() {
      return this.$store.state.categories;
    },
  },
  mounted() {
    this.$store.dispatch("getCategories");
  },
  methods: {
    // getCategories() {
    //   this.$store.dispatch("getCategories");
    // },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.options {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #121111;
  box-shadow: 1px 1px 1px 1px rgb(176, 132, 50);
  border-radius: 3px;
}
.options ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
.options ul li {
  padding: 10px;
  margin: 10px;
  border: 1px solid #080705;
  border-radius: 5px;
  text-align: center;
  background-color: #e2962d;
}

.options ul li:hover {
  background-color: #080705;
  color: #fafafa;
  box-shadow: 1px 1px 1px 1px rgb(252, 251, 248);
}

.to-flex {
  /* display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  flex-wrap: nowrap; */
   display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    width: 100%;
    margin: 1% auto;
    padding: 2% 0;
    gap: 20px;
}

.card{
  /* border-radius: 5px; */
  position: relative;
  box-shadow: 1px 1px 1px 1px rgb(190, 139, 44);
  height: 400px;
}

.pic {
  width: 50%;
  height: auto;
}
</style>
