using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    [Header("Editable Data")]
    public float moveSpeed;
    public float animationSpeed;
    public float jumpPower;

    [Header("Not Editable Data"), Space(20f)]
    [ReadOnly, SerializeField] private bool canJump;
    [ReadOnly, SerializeField] private bool canMove;
    [ReadOnly, SerializeField] private bool isGround;

    [Header("ReadOnly Reference"), Space(20f)]
    [ReadOnly, SerializeField] private Rigidbody _rigidbody;
    [ReadOnly, SerializeField] private Animator _animator;

    private Vector3 velocity;
    private RaycastHit groundRayHit;
    [HideInInspector] public Player player;
    //private static readonly int Attack1 = Animator.StringToHash("Attack");

    private void Awake()
    {
        _rigidbody = GetComponent<Rigidbody>();
        _animator = GetComponent<Animator>();
        player = GetComponent<Player>();
    }

    private void Update()
    {
        CheckGround();
        Move();
        Jump();
    }

    private void CheckGround()
    {
        if (Physics.Raycast(transform.position, Vector3.down, out groundRayHit, Single.PositiveInfinity,
            LayerMask.GetMask("Ground")))
        {
            _animator.SetFloat("GroundDistance", groundRayHit.distance);

            //1f는 Editable한 변수로 제어
            if (groundRayHit.distance > 1f)
            {
                isGround = false;
                _animator.SetBool("isGround", false);
            }
            else
            {
                isGround = true;
                _animator.SetBool("isGround", true);
            }
        }
        else //땅이 존재하지 않을 때 예외처리
        {
            Debug.LogWarning("땅이 존재하지 않을 수 없는데 땅이없다하네 에러임");
            isGround = false;
            _animator.SetBool("isGround", false);
            _animator.SetFloat("GroundDistance", 0f);
        }

    }


    // private enum IndexAnimationType { Attack, Roll, Defense }
    //
    // private void SetTrigger(IndexAnimationType animType, int index)
    // {
    //     _animator.SetTrigger(animType.ToString());
    //     _animator.SetInteger(animType.ToString(), index);
    // }

    public void Roll()
    {
        _animator.SetTrigger("Roll");


        transform.position += Vector3.forward * Time.deltaTime;

    }

    private void Move()
    {
        float inputX = Input.GetAxis("Horizontal");
        float inputY = Input.GetAxis("Vertical");

        velocity = new Vector3(inputX, 0f, inputY) * moveSpeed;

        _animator.SetFloat("VelocityX", inputX);
        _animator.SetFloat("VelocityY", inputY);
        _animator.SetFloat("AnimationSpeed", animationSpeed);

        if (velocity.magnitude > 0f)
        {
            _animator.SetBool("Move", true);
        }
        else
        {
            _animator.SetBool("Move", false);
        }
        transform.position += velocity * Time.deltaTime;
        transform.rotation = Quaternion.LookRotation(new Vector3(inputX, 0f, inputY));
        //_rigidbody.velocity += new Vector3(inputX, 0f, inputY) * (moveSpeed * Time.deltaTime);
    }

    private void Jump()
    {
        canJump = true; // 임시로 박아둔 bool값
        _animator.SetBool("CanJump", canJump);
        if (Input.GetKeyDown(KeyCode.Space) && canJump && isGround)
        {
            _animator.SetTrigger("Jump");
            //_rigidbody.velocity = new Vector3(_rigidbody.velocity.x, jumpPower, _rigidbody.velocity.z);
            _rigidbody.AddForce(Vector3.up * jumpPower, ForceMode.Impulse);
        }
    }
}
