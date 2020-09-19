<template>
  <div id="footer">
      <div class="links">
          <router-link :to="{name: 'Privacy'}" class="font-fix">Privacy</router-link>
          <a href="https://github.com/UCLA-IEEE/project-portal/issues" class="font-fix">Report a bug</a>
      </div>

      <div class="social-media">
          <a href="https://www.facebook.com/groups/uclaieee"><img src="../../public/facebook.png" alt="Facebook"></a>
          <a href="https://www.instagram.com/uclaieee/"><img src="../../public/instagram.png" alt="Instagram"></a>
          <a href="https://uclaieee.slack.com/"><img src="../../public/slack.png" alt="Slack"></a>
          <a href="https://discord.com/invite/yjSQjVb"><img src="../../public/discord.png" alt="Discord"></a>
      </div>
  </div>
</template>

<script>
export default {
    name: "Footer"
}
</script>

<style>
    #footer {
        position: absolute;
        bottom: 0;
        
        display: flex;
        align-items: center;
        justify-content: space-between;

        height: 68px;
        width: 100%;
        padding: 10px 20px;

        background-color: var(--off-white);
    }

    #footer .links a {
        display: block;
        color: var(--off-black);
        text-decoration: none;
    }

    #footer .links a:hover {
        color: var(--gold);
    }

    #footer .social-media img {
        height: 25px;
        margin: 0 10px;
    }

    @media only screen and (min-width: 480px) {
        #footer .links a {
            display: inline;
        }

        #footer .links a:nth-child(2) {
            margin-left: 15px;
        }
    }
</style>