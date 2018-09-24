<template>
  <div class="container">
    <div class="block-wrapper row">
      <div class="col-md-3 col-sm-4" id="sidebar"></div>
      <div class="col-md-9 col-sm-8">
        <div class="row">
          <div class="col-md-12 _pad-vertical-sm">
            <p class="_muted _small">
              Built with ♥ using
            </p>
            <footer>
              <p class="_muted _small">
                <ul class="list-inline">
                  <li v-for="(val, key) in frame" :key="key">
                    <a v-bind="{ href: {val}}"><span class="_tag">{{key}}</span>
                    </a>
                  </li>
                </ul>
              </p>
            </footer>
          </div>
        </div>
      </div>
    </div>
</div>
</template>

<script>
export default {
  name: 'Footer',
  data () {
    return {
      frame: {
        Bootstrap: 'http://getbootstrap.com/',
        Vue: 'https://cn.vuejs.org/index.html'
      }
    }
  }
}
</script>

<style>

</style>
