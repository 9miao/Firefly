firefly
=======

<body class="single single-post postid-31 single-format-standard custom-background single-author singular two-column right-sidebar">
<div id="page" class="hfeed">


	<div id="main">

		<div id="primary">
			<div id="content" role="main">
					
<article id="post-31" class="post-31 post type-post status-publish format-standard hentry category-firefly">
	<header class="entry-header">
		<h1 class="entry-title">Firefly Game Server Framework是什么？</h1>

			</header><!-- .entry-header -->

	<div class="entry-content">
		<p align="left">&nbsp; &nbsp; &nbsp; &nbsp; Firefly是免费、开源、稳定、快速扩展、能 “热更新”的分布式游戏服务器端框架，采用Python编写，基于Twisted框架开发。Firefly的设计理念是“让开发者专注前端”，它包括了开发框架和数据库缓存服务等各种游戏服务器基础服务，节省大量游戏开发的工作时间，真正做到让使用者把精力放在游戏玩法逻辑上。用它可以搭建自定义的分布式架构，只需要修改相应的配置文件即可。</p>
<p align="left"><strong>优势特性</strong><b></b></p>
<ul>
<li>采用单线程多进程架构，支持自定义的分布式架构；</li>
<li>方便的服务器扩展机制，可快速扩展服务器类型和数量；</li>
<li>与客户端采用TCP长连接，无需考虑粘包等问题；</li>
<li>封装数据缓存服务；</li>
<li>可实现实时热更新数据以及游戏逻辑，客户端玩家无感觉；</li>
<li>有几十个基础游戏玩法系统模块提供组装使用（v1.3.0提供）；</li>
</ul>
<p align="left"><strong>框架介绍</strong></p>
<p align="left"><a href="./9miao_files/123.jpg"><img class="alignnone  wp-image-40" alt="123" src="./9miao_files/123.jpg" width="601" height="441"></a></p>
<ul>
<li>management, firefly 是个多进程、分布式的游戏服务器。因此各游戏server(进程)的管理和扩展是firefly很重要的部分，框架通过抽象使服务器的扩展非常容易。</li>
<li>Network，客户端连接通信、server进程间的通信等构成了整个游戏框架的脉络，所有游戏流程都构建在这个脉络上。与客户端的通信采用的是请求/回应式的，所以受到的客户端的请求，服务端都会给出相应的回应，服务端也能主动的推送，广播给客户端消息。这些请求是基于指令号的请求。（例如定义101为登陆指令）server进程之间的通信时采用的异步回调的方式，这样就减少了的进程间通过网络通信中的时间消耗。</li>
<li>Data, 数据处理是网游的重要部分。在网游有大量的数据需要存储，需要更新，这使得数据库的读写效率成为服务器的最大的性能瓶颈。firefly的db处理能够将数据库表中的数据缓存到memcache中并能以对象的形式进行调用相应的对象方法对数据进行操作。可以在不同的进程中通过实例化相同的名称的缓存实例，得到同步的数据。并能将缓存对象中的数据写回数据库中。</li>
</ul>
<p align="left"><strong>框架思路</strong><b></b></p>
<p align="left"><b>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</b>一个最基本的服务器就是一个在不停运行着的应用程序。在分布式游戏服务器中，我们需要的服务器具有的功能有，监听客户端的连接，监听其他服务进程的消息，连接其他的服务进程，有些需要有数据库连接和缓存服务。如下图</p>
<p align="left">&nbsp;<a href="./9miao_files/234.jpg"><img class="alignnone size-full wp-image-41" alt="234" src="./9miao_files/234.jpg" width="552" height="401"></a></p>
<p align="left">net connect 做客户端连接，root监听其他服务进程消息，node连接其他服务进程，db数据库，cache缓存。是否需要监听客户端连接，是否监听其他服务进程消息等这是都是可以在config.json中进行配置。包括各个服务器的名称以及各个服务器之间的连接关系。这样就可以自定义出自己的分布式架构。</p>
			</div><!-- .entry-content -->

</article><!-- #post-31 -->

				
			</div><!-- #content -->
		</div><!-- #primary -->


	</div><!-- #main -->

	<footer id="colophon" role="contentinfo">

			

			<div id="site-generator">


								
			</div>
	</footer><!-- #colophon -->
</div><!-- #page -->

<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F2721c3c016dc1e1ce3c3ca486d58bcf3' type='text/javascript'%3E%3C/script%3E"));
</script><script src="./9miao_files/h.js" type="text/javascript"></script><a href="http://tongji.baidu.com/hm-web/welcome/ico?s=2721c3c016dc1e1ce3c3ca486d58bcf3" target="_blank"><img border="0" src="./9miao_files/21.gif" width="20" height="20"></a>

</body>