<template>
  <div>
    <div class="block-header visible-xs-block">
      <button class="bob navbar-toggle visible-xs" id="menu-show" type="button" data-toggle="collapse" data-target="#menu-mobile">
        <span v-for="item in iconbar" :key="item.id" v-bind="{class:item}"></span>
      </button>

      <div class="navbar-collapse collapse" id="menu-mobile">
        <ul class="nav navbar-nav main-nav">
          <li v-for="item in navlist" :key="item.id">
            <a v-bind="{ href: '#'+item}">{{item}}</a>
          </li>
        </ul>
      </div>
      <a href="."><div class="header-logo"></div></a>
    </div>

    <div class="block-splash" id="top">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <div class="splash-content">
              <div class="splash-logo hidden-xs"></div>
              <h1 class="_white">
                StackOverFlow Survey Analysis
              </h1>
              <h1 class="_white _bold _line-height-small">
                Between 2017 And 2018
              </h1>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="block-wrapper row">
        <div class="col-md-3 col-sm-4" id="sidebar">
          <div class="side-nav hidden-xs" data-offset-top="422" data-spy="affix">
            <div class="logo-nav"></div>
            <ul class="nav main-nav">
              <li v-for="item in navlist" :key="item.id">
                <a v-bind="{ href: '#'+item}">{{item}}</a>
              </li>
            </ul>
            <ul class="back-to-top _muted">
              <li>
                <a href="#top">Back to top<span class="icon"></span></a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  data () {
    return {
      iconbar: ['icon-bar', 'icon-bar', 'icon-bar'],
      navlist: ['Overview', 'DeveloperProfile']
    }
  }
}

</script>

<style>

</style>
