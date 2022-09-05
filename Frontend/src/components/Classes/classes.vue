<template>
  <main class="container">
    <Navbar />
    <section class="model">
      <div class="model-img">
        <img
          class="img"
          src="../../assets/images/model1.jpg"
          alt="Model Image"
        />
      </div>
      <div class="model-text m-1">
        <span class="header-txt">
          Become a Professional Make Up Artist with us
        </span>
        <p>
          <span class="sub-header">
            Style Avenue is the solution to all aspiring make up artists. Learn
            from the best tutors on the best practices to customer service
          </span>
          <br />
          <button class="btn book-btn">
            <a href="/booking">Enroll Today</a>
          </button>
        </p>
      </div>
    </section>
    <section>
      <div class="stats container-fluid">
        <div class="stat">
          <span class="stat-number">25+</span>
          <span class="stat-text">Students</span>
        </div>
        <div class="stat">
          <span class="stat-number">5+</span>
          <span class="stat-text">Instructors</span>
        </div>
        <div class="stat">
          <span class="stat-number">3+</span>
          <span class="stat-text">Courses</span>
        </div>
        <div class="stat">
          <span class="stat-number">200+</span>
          <span class="stat-text">Make Up Products</span>
        </div>
      </div>
    </section>
    <section class="toolkits">
      <div class="card">
        <img
          class="img-fluid kit-img me-3"
          src="../../assets/images/laura-chouette-OCx1FynEGwA-unsplash.jpg"
          alt=""
          srcset=""
        />
      </div>
      <div class="card">
        <img
          class="img-fluid kit-img me-3"
          src="../../assets/images/laura-chouette-OCx1FynEGwA-unsplash.jpg"
          alt=""
          srcset=""
        />
      </div>
    </section>
    <Footer />
  </main>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    Navbar,
    Footer,
  },
};
</script>

<style>
.model {
  display: flex;
  /* justify-content: space-between; */
  /* align-items: center; */
  /* padding: 0 0; */
  /* border: 1px solid red; */
}

.header-txt {
  font-size: 40px !important;
  font-weight: bold;
  /* margin-top: 100px; */
}

.sub-header {
  font-size: 1.4em;
  font-weight: 400;
}

.model-img,
.model-text {
  width: 50%;
  margin: auto auto;
  /* height: 500px; */
  /* border: 1px solid red; */
}

.img {
  width: 100%;
  /* height: 600px; */
  object-fit: cover;
  /* position: center; */
  /* margin: 0 0; */
  /* margin-bottom: 30px; */
}

.stats {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 10px 0;
  box-shadow: 1px 10px 1px 1px rgba(0, 0, 0, 0.1);
  margin-top: -70px;
}

.stat {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 16px 0;
  width: 25%;
  box-sizing: border-box;
  color: #121212;
  font: 1.5rem "Roboto", sans-serif;
  font-weight: inherit;
  background-color: #fafafa;
  border-radius: 5px;
  box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.1);
  margin-right: 10px;
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
}

.stat-text {
  font-size: 1.5rem;
}

.stat:hover {
  background-color: #080705;
  color: #fafafa;
  box-shadow: 1px 1px 1px 1px rgb(252, 251, 248);
}


.kit-img {
  margin: 0 0;
  width: 100%;
  object-fit: cover;
  margin-bottom: 30px;
}

.book-btn {
  background-color: #080705;
  color: #fafafa;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 1.2em;
  font-weight: 500;
  margin-top: 20px;
}

.toolkits {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 0;
  overflow: hidden;
  object-fit: cover;
  /* border: 1px solid red; */
}
</style>