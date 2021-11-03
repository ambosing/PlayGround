using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;
using Spine.Unity;

public class PlayerController : MonoBehaviour
{
    #region Inspector Editable Variables
    [Header("Ediatble Variables")]
    public float speed = 3f;
    public float limitSpeed = 30f;
    public float jumpPower = 10;
    public int jumpCount = 1;
    public float airControlRate = 0.7f;
    public float climbingSpeed = 10f;
    public float fallpower = 1f;

    #endregion

    #region Inspector Show Variables
    [Header("Only Show Variables")]
    [Tooltip("발 아래가 땅인지 아닌지 여부")]
    public bool isGround;
    public bool canClimbing;
    public bool onClimbing;
    #endregion

    private SpriteRenderer renderer;
    private Rigidbody2D _rigidbody2D;
    //private SkeletonAnimation _skeletonAnimation;
    private Animator _anim;


    private void Awake()
    {
        _rigidbody2D = GetComponent<Rigidbody2D>();
        // _skeletonAnimation = GetComponent<SkeletonAnimation>();
        _anim = GetComponent<Animator>();
        renderer = GetComponent<SpriteRenderer>();
    }

    private void Update()
    {

        //AnimationProcess_SkeletonAnimation();

        CheckGround();
        ClimbingMove();
        Jump();


        if (!onClimbing)
        {
            Move__AddForce();

            //Move_VelocityAdd();
            AddFallPower();
            //Move_Transform();
            AnimationProcess_Animator();
        }
    }

    private IEnumerator JumpAni()
    {
        _anim.SetBool("Jump", true);
        yield return new WaitForSeconds(0.1f);
        //while (true)
        //{
        //    if (isGround)
        //        break;
        //    yield return null;
        //}
        yield return new WaitUntil(() => isGround);
        _anim.SetBool("Jump", false);
    }

    #region Climbing Function

    public void ClimbingMove()
    {
        if (!canClimbing)
        {
            ClimbingStateChange(false);
            return;
        }

        if (Mathf.Abs(Input.GetAxisRaw("Vertical")) == 1)
        {
            //위로 올라가기
            ClimbingStateChange(true);
        }

        if (isGround)
            ClimbingStateChange(false);

        float velocityY = Input.GetAxisRaw("Vertical") * climbingSpeed;

        transform.position += new Vector3(0f, velocityY, 0f) * Time.deltaTime;
        
    }

    public void Climbing_Animation()
    {
        if (!canClimbing)
            return;

        if (Input.GetAxisRaw("Vertical") == 1)
        {
            //위로 올라가기
        }

        else if (Input.GetAxisRaw("Vertical") == -1)
        {
            //아치로 올라가기
        }

    }

    

    public void ClimbingStateChange(bool isTrue)
    {
        onClimbing = isTrue;
        if (isTrue)
        {
            _rigidbody2D.gravityScale = 0f;
            _rigidbody2D.velocity = Vector2.zero;
        }
        else
            _rigidbody2D.gravityScale = 1f;
    }

    #endregion

    private void AnimationProcess_Animator()
    {
        switch (Input.GetAxisRaw("Horizontal"))
        {
            case -1:
                renderer.flipX = true;
                _anim.SetBool("Move", true);
                break;
            case 0:
                _anim.SetBool("Move", false);
                break;
            case 1:
                renderer.flipX = false;
                _anim.SetBool("Move", true);
                break;
        }

        //if (_anim.GetBool("Jump") && isGround)
        //{
        //    _anim.SetBool("Jump", false);
        //}

        //if (Input.GetKeyDown(KeyCode.Space) && isGround)
        //{
        //    _anim.SetBool("Jump", true);
        //}
    }

    //private void AnimationProcess_Animator()
    //{
    //    _anim.SetBool("Jump", false);
    //    _anim.SetBool("Move", false);

    //    //이동파
    //    if (Input.GetAxisRaw("Horizontal") != 0)
    //    {
    //        _anim.SetBool("Move", true);
    //        _anim.SetFloat("Horizontal", Input.GetAxisRaw("Horizontal"));
    //    }


    //    // 점프파트
    //    if (!isGround)
    //    {
    //        _anim.SetBool("Jump", true);
    //    }
    //}

    private void AnimationProcess_SkeletonAnimation()
    {
        

        //if (Input.GetKeyDown(KeyCode.A))
        //{
        //    // TODO: SetAnimation은 호출하는 순간 해당 Animation으로 출력
        //    // TODO: AddAnimation은 호출 순간의 애니메이션 종료 후 이어서 나오게 됨
        //    _skeletonAnimation.state.SetAnimation(0, "run_0_l", true);
        //}
        //else if (Input.GetKeyDown(KeyCode.D))
        //{
        //    _skeletonAnimation.state.SetAnimation(0, "run_0", true);
        //}
        //else if (!Input.GetKey(KeyCode.D) && !Input.GetKey(KeyCode.A))
        //{
        //    _skeletonAnimation.state.AddAnimation(0, "idle", true, 1f);
        //}
    }

    private void Move__AddForce()
    {
        float velocityX = Input.GetAxisRaw("Horizontal") * speed * Time.deltaTime;
        _rigidbody2D.AddForce(new Vector2(velocityX, 0f), ForceMode2D.Force);
        // 안움직임
        // _rigidbody2D.AddTorque(speed * Time.deltaTime);
        // 안움직임
        //_rigidbody2D.AddRelativeForce(new Vector2(velocityX, 0f));
    }

    /// <summary>
    /// 캐릭터가 공중에서 떨어지는 판정일 때 떨어지는 속도를 강제로 증가시킨다.
    /// </summary>
    private void AddFallPower()
    {
        if (_rigidbody2D.velocity.y < 0f && !isGround)
        {
            _rigidbody2D.velocity += new Vector2(0f, -fallpower) * Time.deltaTime;
        }
    }


    private void Move_Transform()
    {
        float velocityX = Input.GetAxisRaw("Horizontal") * speed;

        if (!isGround)
        {
            velocityX *= airControlRate;
        }

        transform.position += new Vector3(velocityX, 0f, 0f) * Time.deltaTime;
        //transform.position =
        //    Vector3.MoveTowards(transform.position, transform.position + new Vector3(velocityX, 0f, 0f), 1f);
    }

    private void CheckGround()
    {
        //isGround = Physics2D.Raycast(transform.position, Vector2.down, 0.3f, LayerMask.GetMask("GROUND"));
        var pos = new Vector3(0f, renderer.bounds.size.y * 0.3f);
        var size = new Vector2(1f, 1f);
        var originPos = transform.position - pos;
        Debug.DrawRay(originPos, Vector2.down * 0.2f, Color.red, 0.5f);
        isGround = Physics2D.BoxCast(originPos, size, 0f,
            Vector2.down, 1f, LayerMask.GetMask("GROUND"));
    }

    // Groundcheck를 어디선가 할때만 하게 만드는 방법 - 차이는 변수를 함수로 만들어쓰는 형태
    // 프로퍼ㅌ
    //public bool isGround => Physics2D.Raycast(transform.position, Vector2.down, 0.2f, LayerMask.GetMask("GROUND"));

    private void Move_VelocityAdd()
    {
        float v = Input.GetAxisRaw("Horizontal");

        if (!isGround)
        {
            v *= airControlRate;
        }

        //이동 처리
        if (v != 0)
        {
            // rigidbody2d를 활용한 이동에는 종류가 많음
            // 1.velocity를 사용해서 속력을 강제로 넣어주는 방법
            // 2.AddForce를 사용해서 힘으로 밀어주는 방법
            float velocity = v * speed * Time.deltaTime;
            //_rigidbody2D.velocity = new Vector2(velocity, 0f);
            if (Mathf.Abs(velocity) < limitSpeed)
                _rigidbody2D.velocity += new Vector2(velocity, 0);
        }
    }

    private void Jump()
    {
        Debug.DrawRay(transform.position, Vector2.down * 0.2f, Color.magenta, 0.5f);
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (isGround)
            {
                _rigidbody2D.AddForce(new Vector2(0f, jumpPower), ForceMode2D.Impulse);
                StartCoroutine(JumpAni());
                Debug.Log("땅이 확인되었음");
                jumpCount = 1;
            }
            else if (jumpCount > 0)
            {
                _rigidbody2D.AddForce(new Vector2(0f, jumpPower), ForceMode2D.Impulse);
                jumpCount--;
            }
            else
            {
                Debug.Log("땅이 아님, 점프 못함");
            }
        }
    }
}
