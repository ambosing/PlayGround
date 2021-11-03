using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class PlayerController : MonoBehaviour
{
    [Header("Editable Data")]
    public float moveSpeed;
    public float animationSpeed;
    public float jumpPower;

    [Header("Not Editable Data"), Space(20f)]
    [ReadOnly, SerializeField] private bool canJump = true;
    [ReadOnly, SerializeField] private bool canMove;
    [ReadOnly, SerializeField] private bool isGround;

    [Header("ReadOnly Reference"), Space(20f)]
    [ReadOnly, SerializeField] private Rigidbody _rigidbody;
    [ReadOnly, SerializeField] private Animator _animator;

    private Vector3 velocity;
    private RaycastHit groundRayHit;
    private static readonly int AttackHash = Animator.StringToHash("Attack");

    private void Awake()
    {
        _rigidbody = GetComponent<Rigidbody>();
        _animator = GetComponent<Animator>();
    }

    private void Update()
    {
        Move();
        Jump();
        CheckGround();
        Attack();
    }

    private void Attack()
    {
        if (Input.GetMouseButton(0))
        {
            SetAttackTrigger(0);
        }
    }

    private void SetAttackTrigger(int index)
    {
        _animator.SetTrigger(AttackHash);
        _animator.SetInteger("AttackIndex", 0);
    }

    private void Move()
    {
        float inputX = Input.GetAxisRaw("Horizontal");
        float inputY = Input.GetAxisRaw("Vertical");

        velocity = new Vector3(inputX, 0f, inputY) * moveSpeed;
        transform.position += velocity * Time.deltaTime;

        _animator.SetFloat("VelocityX", inputX);
        _animator.SetFloat("VelocityY", inputY);
        _animator.SetFloat("AnimationSpeed", animationSpeed);

        if (velocity.magnitude > 0)
        {
            _animator.SetBool("Move", true);
        }



        //Debug.Log(inputX + " \t" + inputY);

        
        //_rigidbody.velocity += new Vector3(inputX, 0f, inputY) * (moveSpeed * Time.deltaTime);
    }

    private void Jump()
    {
        _animator.SetBool("CanJump", canJump);
        if (Input.GetKeyDown(KeyCode.Space) && canJump)
        {
            _animator.SetTrigger("Jump");
            _rigidbody.AddForce(Vector3.up * jumpPower, ForceMode.Impulse);
        }
    }

    public void CheckGround()
    {
        if (Physics.Raycast(transform.position, Vector3.down, out groundRayHit,
                        Single.PositiveInfinity, LayerMask.GetMask("Ground")))
        {
            _animator.SetFloat("GroundDistance", groundRayHit.distance);
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
        else
        {
            isGround = false;
            _animator.SetBool("isGround", false);
            _animator.SetFloat("GroundDistance", 0f);
        }

        canJump = isGround ? true : false;
      
    }
}
