# (二叉)树

树部分的题型, 基本都覆盖到了.  
粗浅归纳起来, 就是对四种遍历方式的应用.

1. 需要关注子树的状态时, 就是**后序遍历**, 比如
   * [104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
   * [111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
   * [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)
  
   这时, 递归函数都是有返回值的, `root` 拿到 `left`和`right`的返回后, 再进一步计算出整树的状态, 再返回.
2. 当要求同行, 同层的计算时, 就是**层序遍历**, 比如
   * [513. 找树左下角的值](https://leetcode-cn.com/problems/find-bottom-left-tree-value/)
   * [199. 二叉树的右视图](https://leetcode-cn.com/problems/binary-tree-right-side-view/)

   层序, 需要用队列存储.
3. **前序遍历** 和回溯搭配的较常见, 比如
   * [113. 路径总和 II](https://leetcode-cn.com/problems/path-sum-ii/)
   * [617. 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees/)
   * [450. 删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst/)
   
   前序可以理解为刚进入节点, 或者进入节点之前, 如果需要提前终止的, 基本就是了.
4. **中序遍历** 是从*左树*切换到*右树*, 比如
   * [98. 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)
   
   二叉搜索树很常见. 从左树切到右树, 有时会保存中间量.

其他一些思想点:
1. 递归和回溯, 基本等价. 只是回溯相对普通递归加了额外边界操作.
2. 

难点:
1. 迭代写法.
