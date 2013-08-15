firefly
=======

<!DOCTYPE html>
<!--[if IE 6]>
<html id="ie6" lang="zh-CN">
<![endif]-->
<!--[if IE 7]>
<html id="ie7" lang="zh-CN">
<![endif]-->
<!--[if IE 8]>
<html id="ie8" lang="zh-CN">
<![endif]-->
<!--[if !(IE 6) | !(IE 7) | !(IE 8)  ]><!-->
<html lang="zh-CN">
<!--<![endif]-->
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width" />
<title>Firefly Game Server Framework是什么？ | Firefly Game Server Framework</title>
<link rel="profile" href="http://gmpg.org/xfn/11" />
<link rel="stylesheet" type="text/css" media="all" href="http://firefly.9miao.com/wp-content/themes/twentyeleven/style.css" />
<link rel="pingback" href="http://firefly.9miao.com/xmlrpc.php" />
<!--[if lt IE 9]>
<script src="http://firefly.9miao.com/wp-content/themes/twentyeleven/js/html5.js" type="text/javascript"></script>
<![endif]-->
<link rel="alternate" type="application/rss+xml" title="Firefly Game Server Framework &raquo; Feed" href="http://firefly.9miao.com/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Firefly Game Server Framework &raquo; 评论 Feed" href="http://firefly.9miao.com/?feed=comments-rss2" />
<link rel="alternate" type="application/rss+xml" title="Firefly Game Server Framework &raquo; Firefly Game Server Framework是什么？ 评论 Feed" href="http://firefly.9miao.com/?feed=rss2&#038;p=31" />
<link rel='stylesheet' id='codecolorer-css'  href='http://firefly.9miao.com/wp-content/plugins/codecolorer/codecolorer.css?ver=0.9.9' type='text/css' media='screen' />
<script type='text/javascript' src='http://firefly.9miao.com/wp-includes/js/comment-reply.min.js?ver=3.5.2'></script>
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://firefly.9miao.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="http://firefly.9miao.com/wp-includes/wlwmanifest.xml" /> 
<link rel='prev' title='欢迎来到Firefly开源大家庭！' href='http://firefly.9miao.com/?p=10' />
<link rel='next' title='Firefly alpha v1.2.1 发布，更新如下！' href='http://firefly.9miao.com/?p=45' />
<meta name="generator" content="WordPress 3.5.2" />
<link rel='canonical' href='http://firefly.9miao.com/?p=31' />
	<style type="text/css">.recentcomments a{display:inline !important;padding:0 !important;margin:0 !important;}</style>
<style type="text/css" id="custom-background-css">
body.custom-background { background-color: #ffffff; }
</style>
</head>

<body class="single single-post postid-31 single-format-standard custom-background single-author singular two-column right-sidebar">
<div id="page" class="hfeed">
	<header id="branding" role="banner">
			<hgroup>
				<h1 id="site-title"><span><a href="http://firefly.9miao.com/" title="Firefly Game Server Framework" rel="home">Firefly Game Server Framework</a></span></h1>
				<h2 id="site-description">for python （alpha beta V1.2.1）</h2>
			</hgroup>

						<a href="http://firefly.9miao.com/">
									<img src="http://firefly.9miao.com/wp-content/themes/twentyeleven/images/headers/wheel.jpg" width="1000" height="288" alt="" />
							</a>
			
								<form method="get" id="searchform" action="http://firefly.9miao.com/">
		<label for="s" class="assistive-text">搜索</label>
		<input type="text" class="field" name="s" id="s" placeholder="搜索" />
		<input type="submit" class="submit" name="submit" id="searchsubmit" value="搜索" />
	</form>
			
			<nav id="access" role="navigation">
				<h3 class="assistive-text">主菜单</h3>
								<div class="skip-link"><a class="assistive-text" href="#content" title="跳至主内容区域">跳至主内容区域</a></div>
				<div class="skip-link"><a class="assistive-text" href="#secondary" title="跳至副内容区域">跳至副内容区域</a></div>
								<div class="menu-%e8%ae%ba%e5%9d%9b-container"><ul id="menu-%e8%ae%ba%e5%9d%9b" class="menu"><li id="menu-item-16" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-home menu-item-16"><a href="http://firefly.9miao.com/">Home</a></li>
<li id="menu-item-17" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-17"><a href="http://firefly.9miao.com/?page_id=5">Wiki</a></li>
<li id="menu-item-21" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-21"><a href="http://firefly.9miao.com/?page_id=2">Downloads</a></li>
<li id="menu-item-15" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-15"><a href="http://www.9miao.com/forum-14-1.html">BBS</a></li>
<li id="menu-item-29" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-29"><a href="http://firefly.9miao.com/?page_id=26">开源商用实例（手游）</a></li>
</ul></div>			</nav><!-- #access -->
	</header><!-- #branding -->


	<div id="main">

		<div id="primary">
			<div id="content" role="main">

				
					<nav id="nav-single">
						<h3 class="assistive-text">文章导航</h3>
						<span class="nav-previous"><a href="http://firefly.9miao.com/?p=10" rel="prev"><span class="meta-nav">&larr;</span> 上一篇</a></span>
						<span class="nav-next"><a href="http://firefly.9miao.com/?p=45" rel="next">下一篇 <span class="meta-nav">&rarr;</span></a></span>
					</nav><!-- #nav-single -->

					
<article id="post-31" class="post-31 post type-post status-publish format-standard hentry category-firefly">
	<header class="entry-header">
		<h1 class="entry-title">Firefly Game Server Framework是什么？</h1>

				<div class="entry-meta">
			<span class="sep">发表于 </span><a href="http://firefly.9miao.com/?p=31" title="15:13" rel="bookmark"><time class="entry-date" datetime="2013-08-09T15:13:51+00:00">2013/08/09</time></a><span class="by-author"> <span class="sep"> 由 </span> <span class="author vcard"><a class="url fn n" href="http://firefly.9miao.com/?author=1" title="查看所有由 uxqclm 发布的文章" rel="author">uxqclm</a></span></span>		</div><!-- .entry-meta -->
			</header><!-- .entry-header -->

	<div class="entry-content">
		<p align="left">        Firefly是免费、开源、稳定、快速扩展、能 “热更新”的分布式游戏服务器端框架，采用Python编写，基于Twisted框架开发。Firefly的设计理念是“让开发者专注前端”，它包括了开发框架和数据库缓存服务等各种游戏服务器基础服务，节省大量游戏开发的工作时间，真正做到让使用者把精力放在游戏玩法逻辑上。用它可以搭建自定义的分布式架构，只需要修改相应的配置文件即可。</p>
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
<p align="left"><a href="http://firefly.9miao.com/wp-content/uploads/2013/08/123.jpg"><img class="alignnone  wp-image-40" alt="123" src="http://firefly.9miao.com/wp-content/uploads/2013/08/123.jpg" width="601" height="441" /></a></p>
<ul>
<li>management, firefly 是个多进程、分布式的游戏服务器。因此各游戏server(进程)的管理和扩展是firefly很重要的部分，框架通过抽象使服务器的扩展非常容易。</li>
<li>Network，客户端连接通信、server进程间的通信等构成了整个游戏框架的脉络，所有游戏流程都构建在这个脉络上。与客户端的通信采用的是请求/回应式的，所以受到的客户端的请求，服务端都会给出相应的回应，服务端也能主动的推送，广播给客户端消息。这些请求是基于指令号的请求。（例如定义101为登陆指令）server进程之间的通信时采用的异步回调的方式，这样就减少了的进程间通过网络通信中的时间消耗。</li>
<li>Data, 数据处理是网游的重要部分。在网游有大量的数据需要存储，需要更新，这使得数据库的读写效率成为服务器的最大的性能瓶颈。firefly的db处理能够将数据库表中的数据缓存到memcache中并能以对象的形式进行调用相应的对象方法对数据进行操作。可以在不同的进程中通过实例化相同的名称的缓存实例，得到同步的数据。并能将缓存对象中的数据写回数据库中。</li>
</ul>
<p align="left"><strong>框架思路</strong><b></b></p>
<p align="left"><b>        </b>一个最基本的服务器就是一个在不停运行着的应用程序。在分布式游戏服务器中，我们需要的服务器具有的功能有，监听客户端的连接，监听其他服务进程的消息，连接其他的服务进程，有些需要有数据库连接和缓存服务。如下图</p>
<p align="left"> <a href="http://firefly.9miao.com/wp-content/uploads/2013/08/234.jpg"><img class="alignnone size-full wp-image-41" alt="234" src="http://firefly.9miao.com/wp-content/uploads/2013/08/234.jpg" width="552" height="401" /></a></p>
<p align="left">net connect 做客户端连接，root监听其他服务进程消息，node连接其他服务进程，db数据库，cache缓存。是否需要监听客户端连接，是否监听其他服务进程消息等这是都是可以在config.json中进行配置。包括各个服务器的名称以及各个服务器之间的连接关系。这样就可以自定义出自己的分布式架构。</p>
			</div><!-- .entry-content -->

	<footer class="entry-meta">
		此条目是由 <a href="http://firefly.9miao.com/?author=1">uxqclm</a> 发表在 <a href="http://firefly.9miao.com/?cat=1" title="查看 Firefly相关 中的全部文章" rel="category">Firefly相关</a> 分类目录的。将<a href="http://firefly.9miao.com/?p=31" title="链向 Firefly Game Server Framework是什么？ 的固定链接" rel="bookmark">固定链接</a>加入收藏夹。		
			</footer><!-- .entry-meta -->
</article><!-- #post-31 -->

						<div id="comments">
	
	
			<h2 id="comments-title">
			《<span>Firefly Game Server Framework是什么？</span>》上有 1 条评论		</h2>

		
		<ol class="commentlist">
				<li class="comment even thread-even depth-1" id="li-comment-2">
		<article id="comment-2" class="comment">
			<footer class="comment-meta">
				<div class="comment-author vcard">
					<img alt='' src='http://1.gravatar.com/avatar/b9f2c4fe5fbcaac56727b72af4094bcc?s=68&amp;d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D68&amp;r=G' class='avatar avatar-68 photo' height='68' width='68' /><span class="fn">detours</span> 在 <a href="http://firefly.9miao.com/?p=31#comment-2"><time datetime="2013-08-12T17:21:35+00:00">2013/08/1217:21</time></a> <span class="says">说道：</span>
									</div><!-- .comment-author .vcard -->

				
			</footer>

			<div class="comment-content"><p>顶！</p>
</div>

			<div class="reply">
				<a class='comment-reply-link' href='/?p=31&#038;replytocom=2#respond' onclick='return addComment.moveForm("comment-2", "2", "respond", "31")'>回复 <span>&darr;</span></a>			</div><!-- .reply -->
		</article><!-- #comment-## -->

	</li>
		</ol>

		
		
	
									<div id="respond">
				<h3 id="reply-title">发表评论 <small><a rel="nofollow" id="cancel-comment-reply-link" href="/?p=31#respond" style="display:none;">取消回复</a></small></h3>
									<form action="http://firefly.9miao.com/wp-comments-post.php" method="post" id="commentform">
																			<p class="comment-notes">电子邮件地址不会被公开。 必填项已用 <span class="required">*</span> 标注</p>							<p class="comment-form-author"><label for="author">姓名 <span class="required">*</span></label> <input id="author" name="author" type="text" value="detours" size="30" aria-required='true' /></p>
<p class="comment-form-email"><label for="email">电子邮件 <span class="required">*</span></label> <input id="email" name="email" type="text" value="zm.mu@gmail.com" size="30" aria-required='true' /></p>
<p class="comment-form-url"><label for="url">站点</label><input id="url" name="url" type="text" value="" size="30" /></p>
												<p class="comment-form-comment"><label for="comment">评论</label><textarea id="comment" name="comment" cols="45" rows="8" aria-required="true"></textarea></p>						<p class="form-allowed-tags">您可以使用这些 <abbr title="HyperText Markup Language">HTML</abbr> 标签和属性： <code>&lt;a href=&quot;&quot; title=&quot;&quot;&gt; &lt;abbr title=&quot;&quot;&gt; &lt;acronym title=&quot;&quot;&gt; &lt;b&gt; &lt;blockquote cite=&quot;&quot;&gt; &lt;cite&gt; &lt;code&gt; &lt;del datetime=&quot;&quot;&gt; &lt;em&gt; &lt;i&gt; &lt;q cite=&quot;&quot;&gt; &lt;strike&gt; &lt;strong&gt; </code></p>						<p class="form-submit">
							<input name="submit" type="submit" id="submit" value="发表评论" />
							<input type='hidden' name='comment_post_ID' value='31' id='comment_post_ID' />
<input type='hidden' name='comment_parent' id='comment_parent' value='0' />
						</p>
						<p style="display: none;"><input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="b6102967cd" /></p>					</form>
							</div><!-- #respond -->
						
</div><!-- #comments -->

				
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
</script>
</body>
</html>